from django import forms
from .models import Board, Post, Thread, Attachment


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class PostForm(forms.ModelForm):    # Вообще использовать ModelForm нецелесообразно, ведь заполняется лишь одно поле, да и то вручную.
    board = forms.SlugField(widget=forms.HiddenInput())
    thread = forms.SlugField(widget=forms.HiddenInput(), required=False)
    files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False, label='')
    
    """def __init__(self, board, **kwargs):
        super(PostForm, self).__init__(**kwargs)
        if self.board:
            self.board.widget_attrs = {'value': board}
    """

    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Написать в тред...', 'rows': 5}),
        }
        labels = {
            'content': ''
        }
    
    def save(self, commit=True):
        thread = Thread.objects.get(id=self.cleaned_data['thread'])
        post = Post.objects.create(
                thread = thread,
                content = self.cleaned_data['content']
            )
        post.save()
        
        files = self.cleaned_data['files']
        if files:
            if type(files) != list:
                files = [files]
            for file in files:
                print(file)
                attachment = Attachment.objects.create(
                    file=file,
                    post=post
                )
                attachment.save()
        return post.local_id

    def is_valid(self):
        return super().is_valid() and (self.cleaned_data['content'] or self.cleaned_data['files'])

class ThreadForm(PostForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Заголовок', 'size': 40}), label='')
    field_order = ['title', 'content', 'files']

    class Meta(PostForm.Meta):
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Текст треда', 'rows': 8}),
        }

    def save(self, commit=True):
        board = Board.objects.get(code=self.cleaned_data['board'])
        new_thread = Thread.objects.create(
            board = board,
            title = self.cleaned_data['title']
        )
        self.cleaned_data['thread'] = new_thread.id
        return super().save()

    def is_valid(self):
        return super().is_valid() and (self.cleaned_data['content'] or self.cleaned_data['files'])