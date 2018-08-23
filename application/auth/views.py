from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/auth/newuser",methods = ["GET"])  
def auth_form():
    return render_template("auth/newuser.html", form=UserForm())

@app.route("/auth/", methods=["GET","POST"])
def auth_create():
    form = UserForm(request.form)

    if request.method == "GET":
        return render_template("auth/newuser.html", form = form, user_error="")
 
    if not form.validate():
        return render_template("auth/newuser.html", form = form, user_error="")                   

    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/newuser.html", form = form,
                               user_error = "This username is already in use")
    if not user:
        
        user = User(form.name.data, form.username.data, form.password.data, "basicuser")

    db.session().add(user)
    db.session().commit()
  
    return redirect(url_for("auth_login"))    

@app.route("/admintools/", methods=["GET"])
def admin_form():
    return render_template("auth/admintools.html", form=UserForm(), userlist = User.query.all())

@app.route("/admintools/", methods=["GET", "POST"])    
def admin_tools():
    form = UserForm(request.form)

    userlist= User.query.all()
    return redirect(url_for("songs_index")) 