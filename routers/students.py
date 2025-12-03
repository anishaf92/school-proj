from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.student import Student
from schemas.student import StudentCreate


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        class_name=student.class_name
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# @router.get("/{student_id}/report")
# def get_report(student_id: int, db: Session = Depends(get_db)):
#     student = db.query(Student).filter(Student.id == student_id).first()

#     total = student.maths + student.science + student.english
#     grade = calculate_grade(total)

#     return {
#         "id": student.id,
#         "name": student.name,
#         "class": student.class_name,
#         "marks": {
#             "maths": student.maths,
#             "science": student.science,
#             "english": student.english
#         },
#         "total": total,
#         "grade": grade
#     }
