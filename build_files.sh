# build_files.sh




pip install -r requirements.txt

python3.10 manage.py migrate 
python3.10 manage.py migrate sessions
python3.10 manage.py collectstatic --no-input --clear
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim DJANGO_SUPERUSER_LAST_NAME=fahim python3.9 manage.py createsuperuser --noinput