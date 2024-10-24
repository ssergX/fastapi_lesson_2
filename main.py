from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import create_student, get_student, get_students
from schemas import StudentCreate, Student as StudentSchema
from database import get_db
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Маршрут для создания студента
@app.post("/students/", response_model=StudentSchema)
def create_student_route(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)

# Маршрут для получения студента по ID
@app.get("/students/{student_id}", response_model=StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Маршрут для получения списка студентов
@app.get("/students/", response_model=list[StudentSchema])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = get_students(db, skip=skip, limit=limit)
    return students

