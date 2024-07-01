from app import app, db   # Make sure 'db' is imported correctly
from model import Student, Teacher, Course  # Import the Student model

with app.app_context():
    db.create_all()

    # Create students
    students = [
        {'name': 'zaki', 'email': 'camirzaki15@gmail.com'},
        {'name': 'zako', 'email': 'camirzaki190@gmail.com'},
        {'name': 'zaka', 'email': 'camirzaki192@gmail.com'},
        {'name': 'za', 'email': 'camirzaki194@gmail.com'}
    ]

    student_instances = []
    for student_data in students:
        student = Student(**student_data)
        db.session.add(student)
        student_instances.append(student)

    # Commit students to get their IDs
    db.session.commit()

    # Create teachers
    teachers = [
        {'name': 'hussein', 'email': 'smabo24@gmail.com', 'department': 'computer'},
        {'name': 'ussein', 'email': 'smabo233@gmail.com', 'department': 'computer'},
        {'name': 'hussei', 'email': 'smabo235@gmail.com', 'department': 'computer'},
        {'name': 'huss', 'email': 'smabo234@gmail.com', 'department': 'computer'}
    ]

    teacher_instances = []
    for teacher_data in teachers:
        teacher = Teacher(**teacher_data)
        db.session.add(teacher)
        teacher_instances.append(teacher)

    # Commit teachers to get their IDs
    db.session.commit()

    # Now create courses using the IDs of students and teachers
    courses = [
        {'name': 'Mathematics 101', 'specialization': 'Mathematics', 'grade': 'A', 'student_id': student_instances[0].id, 'teacher_id': teacher_instances[0].id},
        {'name': 'Mathematics 102', 'specialization': 'Mathematics3', 'grade': 'B', 'student_id': student_instances[1].id, 'teacher_id': teacher_instances[1].id},
        {'name': 'Networking', 'specialization': 'Networking', 'grade': 'C', 'student_id': student_instances[2].id, 'teacher_id': teacher_instances[2].id},
        # Add more courses if needed
    ]

    # Add courses to the session
    for course_data in courses:
        course = Course(**course_data)
        db.session.add(course)

    # Commit all changes to the database
    db.session.commit()

print("Seed data added successfully.")



    