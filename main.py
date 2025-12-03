from fastapi import FastAPI
from db.database import Base, engine
from routers import students

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router)


@app.get("/")
def home():
    return {"message": "Student Report Card API running"}
