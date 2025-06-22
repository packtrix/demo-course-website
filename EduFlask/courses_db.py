from app import db
from models import Course

# Create database and tables
db.create_all()

# Sample data
course1 = Course(title='Python for Beginners', description='Learn Python from scratch.', price=499.0)
course2 = Course(title='UPSC Preparation', description='Comprehensive guide to crack UPSC exams.', price=999.0)
course3 = Course(title='Web Development', description='HTML, CSS, JS, Flask tutorials.', price=799.0)

# Add and commit
db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.commit()

print("Courses added successfully!")
