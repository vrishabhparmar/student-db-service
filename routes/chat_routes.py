from flask import Blueprint, request, jsonify
from models.chat_log import ChatLog
from db import SessionLocal

router = Blueprint('chat_routes', __name__)

@router.route('/chats', methods=['POST'])
def log_chat():
    data = request.json
    session = SessionLocal()
    chat = ChatLog(**data)
    session.add(chat)
    session.commit()
    session.close()
    return jsonify({"message": "Chat logged"})
