from flask import Flask
from flask.helpers import url_for


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'very_secret 93f^*f73@+'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app
