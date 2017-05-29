# yet-another-GSC-C-lighthouse
Yet another front end for innovation catalog discover service for GSC China Lighthouse database.
# Promo video about this project
[https://vimeo.com/219328622]

# requriement
Frontend framework Materialize was used materialize-v0.98.0.
Python html2text by Aaron Swartz was used: https://github.com/aaronsw/html2text
```
pip install flask
pip install openpyxl
pip install html2text
pip install Flask-WhooshAlchemy-Redux
pip install sqlalchemy-migrate
pip install flask_wtf
pip install -U pytagcloud
    apt-get install python-pygame
    apt-get build-dep python-pygame
    pip install pygame
    pip install simplejson
pip install -U nltk
```
# A fresh setup sqlite
```
./db_create.py
./dataMigrate.py
./run.py
```
# Rights
used photo https://unsplash.com/photos/GYNxcQvBNzA Rights reserved by Etienne Desclides( https://unsplash.com/@atn )

# Cleanup
```
rm -fr *.db
rm -fr db_repository
```

# Deployment with nginx
```
(env)# apt-get install nginx
(env)# pip install gunicorn
(env)# vi wsgi.py
#!env/bin/python
from app import app
application = app
if __name__ == “__main__”:
    application.run()

(env)# gunicorn -w 4 -b 127.0.0.1:8080 wsgi
```

```
/etc/nginx/sites-available/default
server {
    listen 80;
    server_name inno-search.com;

    location / {
        proxy_pass http://127.0.0.1:8080; # to gunicorn host
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

  }

```
