from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def post_class_id(db: Session, raw_data: schemas.PostClassId):
    class_id: int = raw_data.class_id

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.class_id != class_id))

    join1 = query.first()

    join1 = (
        (join1.to_dict() if hasattr(join1, "to_dict") else vars(join1))
        if join1
        else join1
    )

    res = {
        "join1": join1,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age

    record_to_be_added = {"age": age, "email": email, "full_name": full_name}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def put_students_student_id(db: Session, raw_data: schemas.PutStudentsStudentId):
    student_id: int = raw_data.student_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {
            "age": age,
            "email": email,
            "full_name": full_name,
            "student_id": student_id,
        }.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_courses(db: Session):

    query = db.query(models.Courses)

    courses_all = query.all()
    courses_all = (
        [new_data.to_dict() for new_data in courses_all] if courses_all else courses_all
    )
    res = {
        "courses_all": courses_all,
    }
    return res


async def get_courses_course_id(db: Session, course_id: int):

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))

    courses_one = query.first()

    courses_one = (
        (
            courses_one.to_dict()
            if hasattr(courses_one, "to_dict")
            else vars(courses_one)
        )
        if courses_one
        else courses_one
    )

    res = {
        "courses_one": courses_one,
    }
    return res


async def post_courses(db: Session, raw_data: schemas.PostCourses):
    course_name: str = raw_data.course_name
    instructor_name: str = raw_data.instructor_name

    record_to_be_added = {
        "course_name": course_name,
        "instructor_name": instructor_name,
    }
    new_courses = models.Courses(**record_to_be_added)
    db.add(new_courses)
    db.commit()
    db.refresh(new_courses)
    courses_inserted_record = new_courses.to_dict()

    res = {
        "courses_inserted_record": courses_inserted_record,
    }
    return res


async def put_courses_course_id(db: Session, raw_data: schemas.PutCoursesCourseId):
    course_id: int = raw_data.course_id
    course_name: str = raw_data.course_name
    instructor_name: str = raw_data.instructor_name

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))
    courses_edited_record = query.first()

    if courses_edited_record:
        for key, value in {
            "course_id": course_id,
            "course_name": course_name,
            "instructor_name": instructor_name,
        }.items():
            setattr(courses_edited_record, key, value)

        db.commit()
        db.refresh(courses_edited_record)

        courses_edited_record = (
            courses_edited_record.to_dict()
            if hasattr(courses_edited_record, "to_dict")
            else vars(courses_edited_record)
        )
    res = {
        "courses_edited_record": courses_edited_record,
    }
    return res


async def delete_courses_course_id(db: Session, course_id: int):

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        courses_deleted = record_to_delete.to_dict()
    else:
        courses_deleted = record_to_delete
    res = {
        "courses_deleted": courses_deleted,
    }
    return res


async def get_teachers(db: Session):

    query = db.query(models.Teachers)

    teachers_all = query.all()
    teachers_all = (
        [new_data.to_dict() for new_data in teachers_all]
        if teachers_all
        else teachers_all
    )
    res = {
        "teachers_all": teachers_all,
    }
    return res


async def get_teachers_teacher_id(db: Session, teacher_id: int):

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))

    teachers_one = query.first()

    teachers_one = (
        (
            teachers_one.to_dict()
            if hasattr(teachers_one, "to_dict")
            else vars(teachers_one)
        )
        if teachers_one
        else teachers_one
    )

    res = {
        "teachers_one": teachers_one,
    }
    return res


async def post_teachers(db: Session, raw_data: schemas.PostTeachers):
    name: str = raw_data.name
    subject_specialization: str = raw_data.subject_specialization

    record_to_be_added = {
        "name": name,
        "subject_specialization": subject_specialization,
    }
    new_teachers = models.Teachers(**record_to_be_added)
    db.add(new_teachers)
    db.commit()
    db.refresh(new_teachers)
    teachers_inserted_record = new_teachers.to_dict()

    res = {
        "teachers_inserted_record": teachers_inserted_record,
    }
    return res


async def put_teachers_teacher_id(db: Session, raw_data: schemas.PutTeachersTeacherId):
    teacher_id: int = raw_data.teacher_id
    name: str = raw_data.name
    subject_specialization: str = raw_data.subject_specialization

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))
    teachers_edited_record = query.first()

    if teachers_edited_record:
        for key, value in {
            "name": name,
            "teacher_id": teacher_id,
            "subject_specialization": subject_specialization,
        }.items():
            setattr(teachers_edited_record, key, value)

        db.commit()
        db.refresh(teachers_edited_record)

        teachers_edited_record = (
            teachers_edited_record.to_dict()
            if hasattr(teachers_edited_record, "to_dict")
            else vars(teachers_edited_record)
        )
    res = {
        "teachers_edited_record": teachers_edited_record,
    }
    return res


async def delete_teachers_teacher_id(db: Session, teacher_id: int):

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        teachers_deleted = record_to_delete.to_dict()
    else:
        teachers_deleted = record_to_delete
    res = {
        "teachers_deleted": teachers_deleted,
    }
    return res
