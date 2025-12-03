from sqlalchemy import Column, Integer, String
from db.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    class_name = Column(String)
    maths = Column(Integer, default=0)
    science = Column(Integer, default=0)
    english = Column(Integer, default=0)
