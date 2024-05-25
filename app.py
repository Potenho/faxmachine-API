from flask import Flask
from routes.auth import app as routes
from database.models import db
from database.bcrypt import bcrypt
from flask_jwt_extended import JWTManager
from config.config import Config
from config.registerErrorHandler import registerErrorHandler

app = Flask(__name__, template_folder='static')
app.config.from_object(Config)
registerErrorHandler(app)


def create_app():

    db.init_app(app)
    bcrypt.init_app(app)

    jwt = JWTManager()
    jwt.init_app(app)
    
    app.register_blueprint(routes)
    return app

