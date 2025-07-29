from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Students(BaseModel):
    student_id: int
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None


class ReadStudents(BaseModel):
    student_id: int
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None
    class Config:
        from_attributes = True


class Courses(BaseModel):
    course_id: int
    course_name: Optional[str]=None
    instructor_name: Optional[str]=None


class ReadCourses(BaseModel):
    course_id: int
    course_name: Optional[str]=None
    instructor_name: Optional[str]=None
    class Config:
        from_attributes = True


class Teachers(BaseModel):
    name: Optional[str]=None
    subject_specialization: Optional[str]=None


class ReadTeachers(BaseModel):
    name: Optional[str]=None
    subject_specialization: Optional[str]=None
    class Config:
        from_attributes = True


class Class(BaseModel):
    pass


class ReadClass(BaseModel):
    class Config:
        from_attributes = True




class PostClassId(BaseModel):
    class_id: int = Field(...)

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None

    class Config:
        from_attributes = True



class PutStudentsStudentId(BaseModel):
    student_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None

    class Config:
        from_attributes = True



class PostCourses(BaseModel):
    course_name: Optional[str]=None
    instructor_name: Optional[str]=None

    class Config:
        from_attributes = True



class PutCoursesCourseId(BaseModel):
    course_id: Optional[int]=None
    course_name: Optional[str]=None
    instructor_name: Optional[str]=None

    class Config:
        from_attributes = True



class PostTeachers(BaseModel):
    name: Optional[str]=None
    subject_specialization: Optional[str]=None

    class Config:
        from_attributes = True



class PutTeachersTeacherId(BaseModel):
    teacher_id: Optional[int]=None
    name: Optional[str]=None
    subject_specialization: Optional[str]=None

    class Config:
        from_attributes = True

