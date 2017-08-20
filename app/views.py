from flask import render_template, request, url_for, redirect
from app import app, login_manager
from .forms import LoginForm
from flask_login import login_user
from app.models import User
from flask_login import login_required


@app.route('/')
def landing_page():
    return render_template('landingPage.html')

@app.route('/testy')
@login_required
def testy():
    return "tesy"


@app.route('/base')
def see_base():
    return render_template('base.html')



