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


class Center(Base):
    """description: Represents a training center."""

    __tablename__ = 'centers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)

    def __repr__(self):
        return f"<Center(name={self.name}, location={self.location})>"


class Course(Base):
    """description: Represents a course offered by the training center."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    duration_weeks = Column(Integer)
    center_id = Column(Integer, ForeignKey('centers.id'))

    def __repr__(self):
        return f"<Course(name={self.name}, duration_weeks={self.duration_weeks}, center_id={self.center_id})>"


class Instructor(Base):
    """description: Represents an instructor who teaches courses."""

    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hire_date = Column(DateTime)
    center_id = Column(Integer, ForeignKey('centers.id'))

    def __repr__(self):
        return f"<Instructor(first_name={self.first_name}, last_name={self.last_name}, hire_date={self.hire_date})>"


class Student(Base):
    """description: Represents a student attending courses."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    enrollment_date = Column(DateTime)
    center_id = Column(Integer, ForeignKey('centers.id'))

    def __repr__(self):
        return f"<Student(first_name={self.first_name}, last_name={self.last_name}, enrollment_date={self.enrollment_date})>"


class CourseAssignment(Base):
    """description: Represents the assignment of instructors to courses."""

    __tablename__ = 'course_assignments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    instructor_id = Column(Integer, ForeignKey('instructors.id'))
    assign_date = Column(DateTime)

    def __repr__(self):
        return f"<CourseAssignment(course_id={self.course_id}, instructor_id={self.instructor_id}, assign_date={self.assign_date})>"


class Enrollment(Base):
    """description: Represents student enrollment in courses."""

    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    enrollment_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, enrollment_date={self.enrollment_date})>"


class Attendance(Base):
    """description: Represents student attendance per course session."""

    __tablename__ = 'attendances'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    session_date = Column(DateTime, nullable=False)
    is_present = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Attendance(student_id={self.student_id}, course_id={self.course_id}, session_date={self.session_date}, is_present={self.is_present})>"


class Feedback(Base):
    """description: Stores feedback from students about courses."""

    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    date_submitted = Column(DateTime, nullable=False)
    rating = Column(Integer)
    comments = Column(String)

    def __repr__(self):
        return f"<Feedback(student_id={self.student_id}, course_id={self.course_id}, date_submitted={self.date_submitted}, rating={self.rating})>"


class Session(Base):
    """description: Represents a teaching session for a course."""

    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    session_date = Column(DateTime, nullable=False)
    duration_hours = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Session(course_id={self.course_id}, session_date={self.session_date}, duration_hours={self.duration_hours})>"


class Skill(Base):
    """description: Represents a skill taught in the training center."""

    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Skill(name={self.name})>"


class CourseSkill(Base):
    """description: Represents a connection between courses and skills taught."""

    __tablename__ = 'course_skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))

    def __repr__(self):
        return f"<CourseSkill(course_id={self.course_id}, skill_id={self.skill_id})>"


class StudentSkill(Base):
    """description: Represents a student's skill records."""

    __tablename__ = 'student_skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    proficiency_level = Column(Integer)

    def __repr__(self):
        return f"<StudentSkill(student_id={self.student_id}, skill_id={self.skill_id}, proficiency_level={self.proficiency_level})>"


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Centers
center1 = Center(name="Downtown Train Center", location="Downtown")
center2 = Center(name="Suburban Train Center", location="Suburbs")
center3 = Center(name="Campus Train Center", location="Campus")
center4 = Center(name="City Train Center", location="City")

# Courses
course1 = Course(name="Intro to Programming", description="Basic programming concepts.", duration_weeks=5, center_id=1)
course2 = Course(name="Data Science 101", description="Introduction to data science.", duration_weeks=10, center_id=2)
course3 = Course(name="Advanced AI", description="Deep dive into AI techniques.", duration_weeks=12, center_id=1)
course4 = Course(name="Web Development", description="Frontend and backend web development.", duration_weeks=8, center_id=3)

# Instructors
instructor1 = Instructor(first_name="John", last_name="Doe", hire_date=date(2020, 1, 15), center_id=1)
instructor2 = Instructor(first_name="Jane", last_name="Smith", hire_date=date(2018, 6, 20), center_id=2)
instructor3 = Instructor(first_name="Alice", last_name="Johnson", hire_date=date(2019, 3, 10), center_id=3)
instructor4 = Instructor(first_name="Bob", last_name="Williams", hire_date=date(2021, 11, 5), center_id=1)

# Students
student1 = Student(first_name="Michael", last_name="Chen", enrollment_date=date(2023, 8, 14), center_id=1)
student2 = Student(first_name="Emily", last_name="Clark", enrollment_date=date(2023, 8, 14), center_id=2)
student3 = Student(first_name="Liam", last_name="Brown", enrollment_date=date(2023, 8, 14), center_id=3)
student4 = Student(first_name="Sophia", last_name="Turner", enrollment_date=date(2023, 8, 14), center_id=1)

# Course Assignments
assignment1 = CourseAssignment(course_id=1, instructor_id=1, assign_date=date(2023, 8, 1))
assignment2 = CourseAssignment(course_id=2, instructor_id=2, assign_date=date(2023, 8, 2))
assignment3 = CourseAssignment(course_id=3, instructor_id=3, assign_date=date(2023, 8, 3))
assignment4 = CourseAssignment(course_id=4, instructor_id=4, assign_date=date(2023, 8, 4))

# Enrollments
enrollment1 = Enrollment(student_id=1, course_id=1, enrollment_date=date(2023, 8, 15))
enrollment2 = Enrollment(student_id=2, course_id=2, enrollment_date=date(2023, 8, 16))
enrollment3 = Enrollment(student_id=3, course_id=3, enrollment_date=date(2023, 8, 17))
enrollment4 = Enrollment(student_id=4, course_id=4, enrollment_date=date(2023, 8, 18))

# Attendance
attendance1 = Attendance(student_id=1, course_id=1, session_date=date(2023, 8, 20), is_present=True)
attendance2 = Attendance(student_id=2, course_id=2, session_date=date(2023, 8, 21), is_present=False)
attendance3 = Attendance(student_id=3, course_id=3, session_date=date(2023, 8, 22), is_present=True)
attendance4 = Attendance(student_id=4, course_id=4, session_date=date(2023, 8, 23), is_present=True)

# Feedback
feedback1 = Feedback(student_id=1, course_id=1, date_submitted=date(2023, 8, 25), rating=5, comments="Excellent course")
feedback2 = Feedback(student_id=2, course_id=2, date_submitted=date(2023, 8, 26), rating=4, comments="Very informative")
feedback3 = Feedback(student_id=3, course_id=3, date_submitted=date(2023, 8, 27), rating=3, comments="Good")
feedback4 = Feedback(student_id=4, course_id=4, date_submitted=date(2023, 8, 28), rating=5, comments="Outstanding")

# Sessions
session1 = Session(course_id=1, session_date=date(2023, 8, 20), duration_hours=3)
session2 = Session(course_id=2, session_date=date(2023, 8, 21), duration_hours=3)
session3 = Session(course_id=3, session_date=date(2023, 8, 22), duration_hours=3)
session4 = Session(course_id=4, session_date=date(2023, 8, 23), duration_hours=3)

# Skills
skill1 = Skill(name="Programming Basics")
skill2 = Skill(name="Machine Learning")
skill3 = Skill(name="Web Design")
skill4 = Skill(name="AI Advanced Concepts")

# Course Skills
course_skill1 = CourseSkill(course_id=1, skill_id=1)
course_skill2 = CourseSkill(course_id=2, skill_id=2)
course_skill3 = CourseSkill(course_id=3, skill_id=4)
course_skill4 = CourseSkill(course_id=4, skill_id=3)

# Student Skills
student_skill1 = StudentSkill(student_id=1, skill_id=1, proficiency_level=3)
student_skill2 = StudentSkill(student_id=2, skill_id=2, proficiency_level=4)
student_skill3 = StudentSkill(student_id=3, skill_id=3, proficiency_level=2)
student_skill4 = StudentSkill(student_id=4, skill_id=4, proficiency_level=5)


session.add_all([center1, center2, center3, center4, course1, course2, course3, course4, instructor1, instructor2, instructor3, instructor4, student1, student2, student3, student4, assignment1, assignment2, assignment3, assignment4, enrollment1, enrollment2, enrollment3, enrollment4, attendance1, attendance2, attendance3, attendance4, feedback1, feedback2, feedback3, feedback4, skill1, skill2, skill3, skill4, course_skill1, course_skill2, course_skill3, course_skill4, student_skill1, student_skill2, student_skill3, student_skill4])
session.commit()
