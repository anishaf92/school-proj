from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    class_name: str

class MarksUpdate(BaseModel):
    maths: int | None = None
    science: int | None = None
    english: int | None = None

class StudentOut(BaseModel):
    id: int
    name: str
    class_name: str
    maths: int
    science: int
    english: int

