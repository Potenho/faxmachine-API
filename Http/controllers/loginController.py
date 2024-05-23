from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from database.models import db, User
from database.bcrypt import bcrypt
from forms.forms import RegisterForm, LoginForm


def register():

    data:RegisterForm = RegisterForm(data=request.get_json())

    if not data.validate():
        return jsonify(message="Validation failed", errors=data.errors), 400

    hashedPassword:str = bcrypt.generate_password_hash(data.password.data).decode('utf-8')
    user:User = User(username=data.username.data, password=hashedPassword)
    
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User created", username = user.username), 201




def login():

    data:LoginForm = LoginForm(data=request.get_json())

    if not data.validate():
        return jsonify(message="Validation failed", errors=data.errors), 400
    
    user: User = User.query.filter_by(username=data.username.data).first()
    access_token:str = create_access_token(identity=user.id)

    return jsonify(access_token=access_token), 200