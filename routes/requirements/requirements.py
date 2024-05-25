from flask import jsonify
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import User

class UserRequirements():
    

    def require_login(func):
        """Checks if a given token in Header.Authorization is valid and returns the User object"""
        @wraps(func)
        @jwt_required()
        def decorated_function(*args, **kwargs):
            
            try:
                user_id = get_jwt_identity()
                user = User.query.get(user_id)
            except:
                return jsonify({"error": "Invalid given token"}), 401

            if user is None:
                return jsonify({"error": "User not found"}), 404
            
            return func(user, *args, **kwargs)
        
        
        return decorated_function
