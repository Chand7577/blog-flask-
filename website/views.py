from flask import Blueprint,render_template,flash,request
from flask_login import login_required,current_user

views=Blueprint("views",__name__)

@views.route("/")
@views.route("/home")
@login_required


def home():
    return render_template("home.html",user=current_user)


@views.route('/create-post',methods=["GET","POST"])
@login_required
def create_post():
    if request.method=="POST":
        text=request.form.get("text")

    if not text:
            flash("Post cannot be empty!",category="error")
    else:
         flash("Post has been created !",category="success")
    
    return  render_template('createpost.html',user=current_user)
