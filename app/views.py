from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Manuel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Ana'},
            'body': 'It was nice to see you!'
        },
        {
            'author': {'nickname': 'Francisco'},
            'body': 'I am hungry!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
