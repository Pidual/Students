from flask import Blueprint, jsonify, request
from .models import db,Student

#Crear un blueprint

main = Blueprint('main',__name__)

@main.route('/')
def home():
    return "Hola desde Docker compose + Flask"

#Obtener lista de todos los estudiantes
@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'nombre': s.nombre, 'edad': s.edad, 'carrera': s.carrera} for s in students])


# Add a student
@main.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not all(key in data for key in ["nombre", "edad", "carrera"]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_student = Student(nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({'message': 'Student added', 'student': {'id': new_student.id, 'nombre': new_student.nombre, 'edad': new_student.edad, 'carrera': new_student.carrera}}), 201


# Update student
@main.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': f'Student {student_id} not found'}), 404

    data = request.get_json()
    student.nombre = data.get('nombre', student.nombre)
    student.edad = data.get('edad', student.edad)
    student.carrera = data.get('carrera', student.carrera)

    db.session.commit()
    return jsonify({'message': f'Student {student_id} updated', 'student': {'id': student.id, 'nombre': student.nombre, 'edad': student.edad, 'carrera': student.carrera}}), 200

# Delete student
@main.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': f'Student {student_id} not found'}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': f'Student {student_id} deleted'}), 200