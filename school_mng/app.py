from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db, Student, Teacher, Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Hello, it's me Zaki!"

@app.route('/students', methods=['GET'])
def student_get():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_by_id(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict()), 200

@app.route('/courses', methods=['GET', 'POST'])
def handle_courses():
    if request.method == 'GET':
        courses = Course.query.all()
        return jsonify([course.to_dict() for course in courses]), 200

    elif request.method == 'POST':
        data = request.get_json()
        new_course = Course(
            name=data['name'],
            specialization=data['specialization'],
            grade=data['grade'],
            student_id=data['student_id'],
            teacher_id=data['teacher_id']
        )
        db.session.add(new_course)
        db.session.commit()
        return jsonify(new_course.to_dict()), 201

@app.route('/courses/<int:id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def handle_course(id):
    course = Course.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(course.to_dict()), 200

    elif request.method == 'PATCH' or request.method == 'PUT':
        data = request.get_json()
        course.name = data.get('name', course.name)
        course.specialization = data.get('specialization', course.specialization)
        course.grade = data.get('grade', course.grade)
        course.student_id = data.get('student_id', course.student_id)
        course.teacher_id = data.get('teacher_id', course.teacher_id)
        db.session.commit()
        return jsonify(course.to_dict()), 200

    elif request.method == 'DELETE':
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200

@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([teacher.to_dict() for teacher in teachers]), 200

@app.route('/teachers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(teacher.to_dict()), 200

    elif request.method == 'PATCH':
        data = request.get_json()
        teacher.name = data.get('name', teacher.name)
        teacher.specialization = data.get('specialization', teacher.specialization)
        db.session.commit()
        return jsonify(teacher.to_dict()), 200

    elif request.method == 'DELETE':
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({'message': 'Teacher deleted successfully'}), 200

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    new_teacher = Teacher(name=data['name'], department=data['department'])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify(new_teacher.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5588)





