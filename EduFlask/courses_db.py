from app import db
from models import Course

db.create_all()

# Add only if not already added
if Course.query.count() == 0:
    course1 = Course(title='Python for Beginners', description='Learn Python from scratch.', price=499.0)
    course2 = Course(title='UPSC Preparation', description='Comprehensive guide to crack UPSC exams.', price=999.0)
    course3 = Course(title='Web Development', description='HTML, CSS, JS, Flask tutorials.', price=799.0)

    db.session.add_all([course1, course2, course3])
    db.session.commit()

    print("Courses added successfully!")
else:
    print("Courses already exist!")
