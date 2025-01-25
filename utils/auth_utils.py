from flask import Blueprint, request, jsonify
from ..models.user import User
from ..utils.auth_utils import hash_password, check_password, generate_token

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if User.find_by_username(data['username']):
        return jsonify({"error": "Username already exists"}), 400
        
    user = User(
        username=data['username'],
        password=hash_password(data['password']),
        email=data['email']
    )
    user.save()
    
    return jsonify({"message": "User created successfully"}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.find_by_username(data['username'])
    
    if not user or not check_password(data['password'], user['password']):
        return jsonify({"error": "Invalid credentials"}), 401
        
    token = generate_token(str(user['_id']))
    return jsonify({"token": token}), 200
