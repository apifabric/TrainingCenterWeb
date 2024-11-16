# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class TrainingCenter(Base):
    """description: Represents a training center where courses are conducted."""

    __tablename__ = 'training_center'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Course(Base):
    """description: Represents a course offered by the training center."""

    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    training_center_id = Column(Integer, ForeignKey('training_center.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_hours = Column(Integer)
    instructor_id = Column(Integer, ForeignKey('instructor.id'))


class Instructor(Base):
    """description: Represents an instructor who conducts courses."""

    __tablename__ = 'instructor'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)


class Student(Base):
    """description: Represents a student enrolled in courses."""

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    enrollment_date = Column(Date, nullable=False)


class Enrollment(Base):
    """description: Represents the enrollment of a student in a course."""

    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    enrollment_date = Column(Date, nullable=False)


class Room(Base):
    """description: Represents a room allocated for training purposes."""

    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)


class Schedule(Base):
    """description: Represents the schedule for course sessions."""

    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    scheduled_date = Column(Date, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


class Feedback(Base):
    """description: Represents feedback given by students for a course."""

    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    feedback_text = Column(String)
    feedback_date = Column(Date, nullable=False)


class CourseMaterial(Base):
    """description: Represents materials related to a course."""

    __tablename__ = 'course_material'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    title = Column(String, nullable=False)
    material_type = Column(String)
    release_date = Column(Date)


class Certificate(Base):
    """description: Represents a certificate issued upon course completion."""

    __tablename__ = 'certificate'

    id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer, ForeignKey('enrollment.id'), nullable=False)
    issue_date = Column(Date, nullable=False)
    certificate_type = Column(String)


class Evaluation(Base):
    """description: Represents an evaluation given to students upon course completion."""

    __tablename__ = 'evaluation'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    evaluation_date = Column(Date, nullable=False)
    score = Column(Integer)


class InstructorAssignment(Base):
    """description: Represents the assignment of instructors to courses."""

    __tablename__ = 'instructor_assignment'

    id = Column(Integer, primary_key=True)
    instructor_id = Column(Integer, ForeignKey('instructor.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    assignment_date = Column(Date, nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test Data Creation

from datetime import date

# Training Centers
training_center_1 = TrainingCenter(id=1, name='Tech Academy')
training_center_2 = TrainingCenter(id=2, name='Global Training Center')
training_center_3 = TrainingCenter(id=3, name='Elite Learning Institute')
training_center_4 = TrainingCenter(id=4, name='Skill Builders Center')

# Instructors
instructor_1 = Instructor(id=1, name='Alice Smith', email='alice.smith@example.com')
instructor_2 = Instructor(id=2, name='Bob Jones', email='bob.jones@example.com')
instructor_3 = Instructor(id=3, name='Charlie Brown', email='charlie.brown@example.com')
instructor_4 = Instructor(id=4, name='Dana White', email='dana.white@example.com')

# Students
student_1 = Student(id=1, name='John Doe', email='john.doe@example.com', enrollment_date=date(2023, 1, 15))
student_2 = Student(id=2, name='Jane Roe', email='jane.roe@example.com', enrollment_date=date(2023, 2, 20))
student_3 = Student(id=3, name='Alan Smith', email='alan.smith@example.com', enrollment_date=date(2023, 3, 25))
student_4 = Student(id=4, name='Nancy Drew', email='nancy.drew@example.com', enrollment_date=date(2023, 4, 10))

# Courses
course_1 = Course(id=1, name='Python Programming', training_center_id=1, start_date=date(2023, 1, 10), end_date=date(2023, 3, 10), total_hours=60, instructor_id=1)
course_2 = Course(id=2, name='Data Science Fundamentals', training_center_id=2, start_date=date(2023, 2, 5), end_date=date(2023, 4, 5), total_hours=70, instructor_id=2)
course_3 = Course(id=3, name='Web Development', training_center_id=3, start_date=date(2023, 3, 15), end_date=date(2023, 5, 15), total_hours=80, instructor_id=3)
course_4 = Course(id=4, name='Cyber Security', training_center_id=4, start_date=date(2023, 4, 20), end_date=date(2023, 6, 20), total_hours=50, instructor_id=4)

# Enrollments
enrollment_1 = Enrollment(id=1, student_id=1, course_id=1, enrollment_date=date(2023, 1, 16))
enrollment_2 = Enrollment(id=2, student_id=2, course_id=2, enrollment_date=date(2023, 2, 22))
enrollment_3 = Enrollment(id=3, student_id=3, course_id=3, enrollment_date=date(2023, 3, 28))
enrollment_4 = Enrollment(id=4, student_id=4, course_id=4, enrollment_date=date(2023, 4, 12))

# Rooms
room_1 = Room(id=1, name='Room A', capacity=30)
room_2 = Room(id=2, name='Room B', capacity=25)
room_3 = Room(id=3, name='Room C', capacity=20)
room_4 = Room(id=4, name='Room D', capacity=35)

# Schedules
schedule_1 = Schedule(id=1, course_id=1, room_id=1, scheduled_date=date(2023, 1, 20), start_time=datetime(2023, 1, 20, 9, 0), end_time=datetime(2023, 1, 20, 17, 0))
schedule_2 = Schedule(id=2, course_id=2, room_id=2, scheduled_date=date(2023, 2, 25), start_time=datetime(2023, 2, 25, 10, 0), end_time=datetime(2023, 2, 25, 18, 0))
schedule_3 = Schedule(id=3, course_id=3, room_id=3, scheduled_date=date(2023, 3, 30), start_time=datetime(2023, 3, 30, 9, 0), end_time=datetime(2023, 3, 30, 17, 0))
schedule_4 = Schedule(id=4, course_id=4, room_id=4, scheduled_date=date(2023, 4, 15), start_time=datetime(2023, 4, 15, 10, 0), end_time=datetime(2023, 4, 15, 18, 0))

# Feedback
feedback_1 = Feedback(id=1, course_id=1, student_id=1, feedback_text='Great course!', feedback_date=date(2023, 3, 11))
feedback_2 = Feedback(id=2, course_id=2, student_id=2, feedback_text='Very informative.', feedback_date=date(2023, 4, 6))
feedback_3 = Feedback(id=3, course_id=3, student_id=3, feedback_text='Well organized.', feedback_date=date(2023, 5, 16))
feedback_4 = Feedback(id=4, course_id=4, student_id=4, feedback_text='Highly recommend.', feedback_date=date(2023, 6, 21))

# Course Materials
course_material_1 = CourseMaterial(id=1, course_id=1, title='Introduction to Python', material_type='PDF', release_date=date(2023, 1, 12))
course_material_2 = CourseMaterial(id=2, course_id=2, title='Data Science Essentials', material_type='Book', release_date=date(2023, 2, 8))
course_material_3 = CourseMaterial(id=3, course_id=3, title='HTML Crash Course', material_type='Video', release_date=date(2023, 3, 18))
course_material_4 = CourseMaterial(id=4, course_id=4, title='Cyber Defense Techniques', material_type='Article', release_date=date(2023, 4, 22))

# Certificates
certificate_1 = Certificate(id=1, enrollment_id=1, issue_date=date(2023, 3, 12), certificate_type='Completion')
certificate_2 = Certificate(id=2, enrollment_id=2, issue_date=date(2023, 4, 7), certificate_type='Completion')
certificate_3 = Certificate(id=3, enrollment_id=3, issue_date=date(2023, 5, 17), certificate_type='Excellence')
certificate_4 = Certificate(id=4, enrollment_id=4, issue_date=date(2023, 6, 22), certificate_type='Completion')

# Evaluations
evaluation_1 = Evaluation(id=1, course_id=1, student_id=1, evaluation_date=date(2023, 3, 13), score=85)
evaluation_2 = Evaluation(id=2, course_id=2, student_id=2, evaluation_date=date(2023, 4, 8), score=90)
evaluation_3 = Evaluation(id=3, course_id=3, student_id=3, evaluation_date=date(2023, 5, 18), score=88)
evaluation_4 = Evaluation(id=4, course_id=4, student_id=4, evaluation_date=date(2023, 6, 23), score=92)


session.add_all([training_center_1, training_center_2, training_center_3, training_center_4, instructor_1, instructor_2, instructor_3, instructor_4, student_1, student_2, student_3, student_4, course_1, course_2, course_3, course_4, enrollment_1, enrollment_2, enrollment_3, enrollment_4, room_1, room_2, room_3, room_4, schedule_1, schedule_2, schedule_3, schedule_4, feedback_1, feedback_2, feedback_3, feedback_4, course_material_1, course_material_2, course_material_3, course_material_4, certificate_1, certificate_2, certificate_3, certificate_4, evaluation_1, evaluation_2, evaluation_3, evaluation_4])
session.commit()
