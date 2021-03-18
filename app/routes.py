from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Matheus'}
    posts = [
        {'author': {'username': 'Maria'}, 'body': "Olá da Maria"},
        {'author': {'username': 'Matheus'}, 'body': "Olá"},
        {'author': {'username': 'Aline'}, 'body': "Olá, pessoal!"}
    ]
    return render_template("index.html", user=user, posts=posts)