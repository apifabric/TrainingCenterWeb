# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 16, 2024 15:49:21
# Database: sqlite:////tmp/tmp.KADeKrFjPD-01JCTTHYRS0G8BZ0WE5PT2ZRKR/TrainingCenterProject/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Instructor(SAFRSBaseX, Base):
    """
    description: Represents an instructor who conducts courses.
    """
    __tablename__ = 'instructor'
    _s_collection_name = 'Instructor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CourseList : Mapped[List["Course"]] = relationship(back_populates="instructor")
    InstructorAssignmentList : Mapped[List["InstructorAssignment"]] = relationship(back_populates="instructor")



class Room(SAFRSBaseX, Base):
    """
    description: Represents a room allocated for training purposes.
    """
    __tablename__ = 'room'
    _s_collection_name = 'Room'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="room")



class Student(SAFRSBaseX, Base):
    """
    description: Represents a student enrolled in courses.
    """
    __tablename__ = 'student'
    _s_collection_name = 'Student'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    enrollment_date = Column(Date, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="student")
    EvaluationList : Mapped[List["Evaluation"]] = relationship(back_populates="student")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="student")



class TrainingCenter(SAFRSBaseX, Base):
    """
    description: Represents a training center where courses are conducted.
    """
    __tablename__ = 'training_center'
    _s_collection_name = 'TrainingCenter'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    CourseList : Mapped[List["Course"]] = relationship(back_populates="training_center")



class Course(SAFRSBaseX, Base):
    """
    description: Represents a course offered by the training center.
    """
    __tablename__ = 'course'
    _s_collection_name = 'Course'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    training_center_id = Column(ForeignKey('training_center.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_hours = Column(Integer)
    instructor_id = Column(ForeignKey('instructor.id'))

    # parent relationships (access parent)
    instructor : Mapped["Instructor"] = relationship(back_populates=("CourseList"))
    training_center : Mapped["TrainingCenter"] = relationship(back_populates=("CourseList"))

    # child relationships (access children)
    CourseMaterialList : Mapped[List["CourseMaterial"]] = relationship(back_populates="course")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="course")
    EvaluationList : Mapped[List["Evaluation"]] = relationship(back_populates="course")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="course")
    InstructorAssignmentList : Mapped[List["InstructorAssignment"]] = relationship(back_populates="course")
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="course")



class CourseMaterial(SAFRSBaseX, Base):
    """
    description: Represents materials related to a course.
    """
    __tablename__ = 'course_material'
    _s_collection_name = 'CourseMaterial'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    title = Column(String, nullable=False)
    material_type = Column(String)
    release_date = Column(Date)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("CourseMaterialList"))

    # child relationships (access children)



class Enrollment(SAFRSBaseX, Base):
    """
    description: Represents the enrollment of a student in a course.
    """
    __tablename__ = 'enrollment'
    _s_collection_name = 'Enrollment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'), nullable=False)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    enrollment_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("EnrollmentList"))
    student : Mapped["Student"] = relationship(back_populates=("EnrollmentList"))

    # child relationships (access children)
    CertificateList : Mapped[List["Certificate"]] = relationship(back_populates="enrollment")



class Evaluation(SAFRSBaseX, Base):
    """
    description: Represents an evaluation given to students upon course completion.
    """
    __tablename__ = 'evaluation'
    _s_collection_name = 'Evaluation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    student_id = Column(ForeignKey('student.id'), nullable=False)
    evaluation_date = Column(Date, nullable=False)
    score = Column(Integer)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("EvaluationList"))
    student : Mapped["Student"] = relationship(back_populates=("EvaluationList"))

    # child relationships (access children)



class Feedback(SAFRSBaseX, Base):
    """
    description: Represents feedback given by students for a course.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    student_id = Column(ForeignKey('student.id'), nullable=False)
    feedback_text = Column(String)
    feedback_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("FeedbackList"))
    student : Mapped["Student"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class InstructorAssignment(SAFRSBaseX, Base):
    """
    description: Represents the assignment of instructors to courses.
    """
    __tablename__ = 'instructor_assignment'
    _s_collection_name = 'InstructorAssignment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    instructor_id = Column(ForeignKey('instructor.id'), nullable=False)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    assignment_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("InstructorAssignmentList"))
    instructor : Mapped["Instructor"] = relationship(back_populates=("InstructorAssignmentList"))

    # child relationships (access children)



class Schedule(SAFRSBaseX, Base):
    """
    description: Represents the schedule for course sessions.
    """
    __tablename__ = 'schedule'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    course_id = Column(ForeignKey('course.id'), nullable=False)
    room_id = Column(ForeignKey('room.id'), nullable=False)
    scheduled_date = Column(Date, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("ScheduleList"))
    room : Mapped["Room"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class Certificate(SAFRSBaseX, Base):
    """
    description: Represents a certificate issued upon course completion.
    """
    __tablename__ = 'certificate'
    _s_collection_name = 'Certificate'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    enrollment_id = Column(ForeignKey('enrollment.id'), nullable=False)
    issue_date = Column(Date, nullable=False)
    certificate_type = Column(String)

    # parent relationships (access parent)
    enrollment : Mapped["Enrollment"] = relationship(back_populates=("CertificateList"))

    # child relationships (access children)
