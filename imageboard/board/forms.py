from django import forms
from .models import Post, Thread, Attachment


class PostForm(forms.ModelForm):
    board = forms.SlugField(widget=forms.HiddenInput())
    thread = forms.SlugField(widget=forms.HiddenInput())
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    
    """def __init__(self, board, **kwargs):
        super(PostForm, self).__init__(**kwargs)
        if self.board:
            self.board.widget_attrs = {'value': board}
    """

    class Meta:
        model = Post
        fields = ['content']
    
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

    def is_valid(self):
        return super(PostForm, self).is_valid() and (self.cleaned_data['content'] or self.cleaned_data['files'])

