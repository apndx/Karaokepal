# application/auth/views.py

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm

# Getting and posting the login form
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))  

# Logout
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

# Getting the newuser form
@app.route("/auth/newuser",methods = ["GET"])  
def auth_form():
    return render_template("auth/newuser.html", form=UserForm())

# Creating a new user
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

# Getting the admintools
@app.route("/admintools/", methods=["GET"])
@login_required(role="ADMIN")
def admin_form():
    return render_template("auth/admintools.html", form=UserForm(), userlist = User.query.order_by(User.name).all())

# Creating a userlist for admintools
@app.route("/admintools/", methods=["GET", "POST"])    
@login_required(role="ADMIN")
def admin_tools():
    return redirect(url_for("songs_index")) 
  
@app.route("/admintools/<user_id>/", methods=["GET"])
@login_required(role="ADMIN")
def user_change(user_id):
    
    user = User.query.get(user_id)
    form= UserForm(obj=user)
    
    if not form.validate():
        return render_template("auth/change.html", user=user,  form= form, user_error="" )

    return render_template("auth/change.html", user=user,  form= form ) 

# Admin can change the name and the password for the user
@app.route("/admintools/<user_id>", methods=["POST"]) 
@login_required(role="ADMIN")
def change_user_form(user_id):      
    user = User.query.get(user_id)
    form = UserForm(obj=user) # the form is prefilled with data

    if not form.validate():
        return render_template("auth/change.html", form = form, user=user)

    user.name = form.name.data
    user.password = form.password.data

    db.session().commit()

    return redirect(url_for("admintools")) 

# Admin can delete a user
@app.route("/admintools/<user_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def user_delete(user_id):
    user = User.query.get(user_id)
    form = UserForm(obj=user) # the form is prefilled with data

    if user == current_user:
        return render_template("auth/admintools.html", users = User.query.all(), form=form,
                               user_error = "You cannot remove your own account")

    db.session().delete(user)
    db.session().commit()    

    return redirect(url_for("admintools")) 

@app.route("/admintools/", methods=["GET"])
@login_required(role="ADMIN")
def admintools():
    return render_template("auth/admintools.html", users = User.query.all())

# Admin can change the status of a user
@app.route("/admintools/<user_id>/status/", methods=["GET","POST"])
@login_required(role="ADMIN")
def change_user_status(user_id):

    user = User.query.get(user_id)
    form= UserForm(obj=user)

    if user == current_user:
        return render_template("auth/admintools.html", users = User.query.all(), form=form,
                               user_error = "You cannot remove your own admin status")

    if user.user_role == "admin":
        user.user_role = "basicuser"
    else:
        user.user_role = "admin"

    db.session().commit()

    return redirect(url_for("admintools")) 