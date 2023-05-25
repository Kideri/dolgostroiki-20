cd /app && python manage.py migrate

cd /app && python manage.py collectstatic --no-input --clear

cd /app && uwsgi --ini uwsgi.ini
