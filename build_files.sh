# build_files.sh



python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 --version
python3 manage.py migrate 
python3 manage.py migrate sessions
python3 manage.py collectstatic 
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim DJANGO_SUPERUSER_LAST_NAME=fahim python3.9 manage.py createsuperuser --noinput
