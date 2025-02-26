import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),    
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')


    # initialize the app with the extension
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import db models
    from .database.models import User

    with app.app_context():
        db.create_all()

    #  register views
    from .views.front import frontend
    from .views.dashboard import dashboard
    app.register_blueprint(frontend)
    app.register_blueprint(dashboard)

    
    

    return app