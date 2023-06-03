from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "u313195186_testbcom"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uownwnwoewd sdwsdfsd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u313195186_askformoore:Olaoluwa123@srv996.hstgr.io/u313195186_testbcom'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # Takes the DB and tells flask the app to use with it.

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from webapp import models  # Makes sure our models are loaded before app launch.

    with app.app_context():
        db.create_all()

    return app

# Depreciated and replaced with appcontext
# def create_database(appy):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=appy)
#         print('Created Database!')
#     elif path.exists('website/' + DB_NAME):
#         print('Database already Exists')
