from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/class/id')
async def post_class_id(raw_data: schemas.PostClassId, db: Session = Depends(get_db)):
    try:
        return await service.post_class_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(raw_data: schemas.PutStudentsStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/')
async def get_courses(db: Session = Depends(get_db)):
    try:
        return await service.get_courses(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/course_id')
async def get_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_courses_course_id(db, course_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/courses/')
async def post_courses(raw_data: schemas.PostCourses, db: Session = Depends(get_db)):
    try:
        return await service.post_courses(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/courses/course_id/')
async def put_courses_course_id(raw_data: schemas.PutCoursesCourseId, db: Session = Depends(get_db)):
    try:
        return await service.put_courses_course_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/courses/course_id')
async def delete_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_courses_course_id(db, course_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teachers/')
async def get_teachers(db: Session = Depends(get_db)):
    try:
        return await service.get_teachers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teachers/teacher_id')
async def get_teachers_teacher_id(teacher_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_teachers_teacher_id(db, teacher_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teachers/')
async def post_teachers(raw_data: schemas.PostTeachers, db: Session = Depends(get_db)):
    try:
        return await service.post_teachers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teachers/teacher_id/')
async def put_teachers_teacher_id(raw_data: schemas.PutTeachersTeacherId, db: Session = Depends(get_db)):
    try:
        return await service.put_teachers_teacher_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/teachers/teacher_id')
async def delete_teachers_teacher_id(teacher_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_teachers_teacher_id(db, teacher_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

