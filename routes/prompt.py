from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

prompt = Blueprint('prompt', __name__)

@prompt.route('/prompt', methods=['POST'])
@jwt_required()
def handle_prompt():
    current_user = get_jwt_identity()
    data = request.get_json()
    user_prompt = data.get('prompt')
    client.flow.execute("FLOW_NAME", user_prompt)
    return jsonify({
        "message": "Prompt received",
        "prompt": user_prompt,
        "user": current_user
    }), 200
