from app import app
from flask import render_template, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Панель управления')

@app.route('/login')
def login():
    return render_template('login.html', title='Вход')

@app.route('/register')
def register():
    return render_template('register.html', title='Регистрация')

@app.route('/hello')
def hello_page():
    return render_template('hello.html', title='Тевирп!')