web: gunicorn PublicChatRoom.wsgi --log-file -
release: python3 manage.py makemigrations --noinput
release:python3 manage.py collectstatic --noinput
release: python3 manage.py migrate --nopipinput