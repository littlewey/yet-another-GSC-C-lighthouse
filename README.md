# yet-another-GSC-C-lighthouse
Yet another front end for innovation catalog discover service for GSC China Lighthouse database.

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
```
# A fresh setup sqlite
```
./db_create.py
./dataMigrate.py
./run.py
```
# Cleanup
```
rm -fr *.db
rm -fr db_repository
```
