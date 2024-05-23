from flask import Flask
from routes.routes import app as routes
from database.models import db
from database.bcrypt import bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta


def create_app():
    app = Flask(__name__, template_folder='static')
    app.config['SECRET_KEY'] = '660652117f2951272aa25cfe8dbc540c'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faxmachine.db' 
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
    app.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "token"
    
    db.init_app(app)
    bcrypt.init_app(app)

    jwt = JWTManager()
    jwt.init_app(app)
    
    app.register_blueprint(routes)
    return app

    


if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()
        
    app.run(debug=True)