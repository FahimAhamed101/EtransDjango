# build_files.sh


<<<<<<< HEAD

=======
>>>>>>> 8efc7fa98e4805a4b2d3398fcd17ee9ca5049aa2
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py makemigrations
python3 --version
python3 manage.py migrate 
python3 manage.py migrate sessions
python3 manage.py collectstatic 
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim DJANGO_SUPERUSER_LAST_NAME=fahim python3 manage.py createsuperuser --noinput
