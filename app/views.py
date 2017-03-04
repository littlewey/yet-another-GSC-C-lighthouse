from flask import render_template
from app import app
from app import db, models
@app.route('/')
@app.route('/index')
def index():
    tools = [  # fake array of tools
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='yalh',
                           developer=developer,
                           tools=tools)
@app.route('/developer/<developerName>')
def developer(developerName):
    developer = models.Developer.query.filter(models.Developer.NameString == developerName).first()
    tools = [  # fake array of tools
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print type(developerName)
    return render_template("index.html",
                           title=developerName,
                           developer=developer,
                           tools=tools)
