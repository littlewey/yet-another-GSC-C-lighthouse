from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
class SearchForm(FlaskForm):
    search = StringField('search')