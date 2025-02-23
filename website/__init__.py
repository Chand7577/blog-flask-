from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# setting up database

db=SQLAlchemy()

DB_NAME='blogs.db'

def create_app():
    app=Flask(__name__) # initialization of the app
    app.config["SECRET_KEY"]="ram"
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    from .views import views
    from .auth import auth
    from .models import User

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    create_db(app)

    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

   

    return app


def create_db(app):
    if not path.exists("website/"+ DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created database")






