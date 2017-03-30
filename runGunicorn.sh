env/bin/python gunicorn -w 4 -b 127.0.0.1:8080 wsgi --reload
service nginx restart
