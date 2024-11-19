from app import db
from models import User, Class

db.create_all()

# Add sample users
student = User(username='student1', role='student')
student.set_password('password')
teacher = User(username='teacher1', role='teacher')
teacher.set_password('password')
admin = User(username='admin1', role='admin')
admin.set_password('password')

# Add sample classes
class1 = Class(name='CSE 101', capacity=30, teacher_id=2)
class2 = Class(name='CSE 102', capacity=25, teacher_id=2)

db.session.add_all([student, teacher, admin, class1, class2])
db.session.commit()
