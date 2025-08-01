from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    full_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    age = Column(Integer, primary_key=False)


class Courses(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String, primary_key=False)
    instructor_name = Column(String, primary_key=False)


class Teachers(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, primary_key=False)
    subject_specialization = Column(String, primary_key=False)


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True, autoincrement=True)


