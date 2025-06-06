from flask import Blueprint, request, jsonify
from models.student import Student
from db import SessionLocal

router = Blueprint('student_routes', __name__)

@router.route('/students', methods=['POST'])
def create_student():
    data = request.json
    session = SessionLocal()
    student = Student(**data)
    session.add(student)
    session.commit()
    session.refresh(student)
    session.close()
    return jsonify({"message": "Student created", "id": student.id})

@router.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    session.close()
    if not student:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "name": student.name,
        "email": student.email,
        "risk_prediction": student.risk_prediction
    })
