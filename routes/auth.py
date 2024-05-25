from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from database.models import db, User
from database.bcrypt import bcrypt
from forms.forms import RegisterForm, LoginForm, ChangePasswordForm
from routes.requirements.requirements import UserRequirements

app = Blueprint('auth',__name__)


@app.route("/user/register", methods=["POST"] )
def register():

    data: RegisterForm = RegisterForm(data=request.get_json())

    if not data.validate():
        return jsonify(message="Validation failed", errors=data.errors), 400

    hashedPassword: str = bcrypt.generate_password_hash(data.password.data).decode('utf-8')
    user: User = User(username=data.username.data, password=hashedPassword)
    
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User created", username = user.username), 201




@app.route("/user/login", methods=["POST"] )
def login():

    data: LoginForm = LoginForm(data=request.get_json())

    if not data.validate():
        return jsonify(message="Validation failed", errors=data.errors), 400
    
    user: User = User.query.filter_by(username=data.username.data).first()
    access_token: str = create_access_token(identity=user.id)

    return jsonify(access_token=access_token), 200


@app.route("/user/change-password",  methods=["PATCH"])
@UserRequirements.require_login
def changePassword(user: User):
    data: ChangePasswordForm = ChangePasswordForm(data=request.get_json())

    if not data.validate():
        return jsonify(message="Validation failed", errors=data.errors), 400

    if not bcrypt.check_password_hash(user.password, data.previous_password.data):
        return jsonify(error="The user's password doesn't match previous_password"), 403
    
    hashedPassword: str = bcrypt.generate_password_hash(data.new_password.data).decode('utf-8')
    user.password = hashedPassword
    db.session.commit()

    return jsonify(user_id=user.username), 200