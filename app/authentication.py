from app import login_manager, db, app
from app.utilities import translate, is_safe_url
from app.models import User, Gender
from flask_login import login_required, login_user, logout_user
from flask import request, render_template, url_for, redirect
from app.forms import SignupForm, LoginForm
from app.views import landing_page

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    return user

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if request.method == 'GET':  # if not form.validate_on_submit():
        return render_template(
            'login2.html',
            form=form
        )

    elif request.method == 'POST':

        print(url_for('landing_page'))
        user = User.query.filter(
            User.username==request.form['username']
        ).first()

        pw_correct = user.verify_password(request.form['password'])
        if (pw_correct and user is not None):
            login_user(user)
            next = request.args.get('next') or request.form['next'] or ""
            if not is_safe_url(next):
                return flask.abort(400)
            return redirect(next or url_for('landing_page')) 
        else:
            return u"اطلاعات وارد شده معتبر نیستند"   
        

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing_page'))

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    print(request.form)

    fr = LoginForm()
    if request.method == 'POST' and fr.validate_on_submit():
 
        new_user = User(
            firstname = request.form['firstname'],
            lastname = request.form['lastname'],
            username = request.form['username'],
        )

        new_user.gender = Gender.query.filter_by(title=request.form['gender']).first()
                
        new_user.set_password(request.form['password'])
        db.session.add(new_user)
        db.session.commit()

        return "signed up successfully"

    return render_template(
        'signup.html',
        form=fr
    )


@login_manager.unauthorized_handler
def unauthrized():
    return redirect(url_for('login', next=request.url))
    