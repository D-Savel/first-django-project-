# first-django-project-
First app with Django

## Getting started for local running

### Environment

- Clone the repo into your project directory: `git clone https://github.com/D-Savel/first-django-project-.git`
- if you don't have victual machine: `pip install virtualenv`
- install vurtual env: `virtualenv env -p python3`
- activate virtual env: `. env/bin/activate`
- `cd first-django-project-`
- install the requirements: `pip install -r requirements.txt`
- make migrations :
  `python3 manage.py makemigrations`
  `python3 manage.py migrate`

Then run Django server:
  
  ```sh
  cd first-django-project-/firstProject
  python3 manage.py runserver
  ```

If you want to activate livereload:

```sh
. env/bin/activate
cd first-django-project-/firstProject
python3 manage.py livereload
```


Open http://127.0.0.1:8000/home/ in web browser
