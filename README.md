simple django imageboard engine

# Installation
In principle, you should follow this steps:
1. Install requirements
```bash
pip install -r requirements.txt
```
2. Make and apply migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
3. Run server
```bash
python manage.py runserver
```
You can specify address to host to the outside
```bash
python manage.py runserver 0.0.0.0:5000
```
(port 5000 is just example)

Then open at http://localhost:yourport


If you want to use admin panel, create superuser via:
```bash
python manage.py createsuperuser
```

I hope I make everything clear
