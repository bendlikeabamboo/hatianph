from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ASDF"
    
    from .views import views
    from .auth import auth
    from .contact import contact

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(contact, url_prefix="/contact/")

    return app