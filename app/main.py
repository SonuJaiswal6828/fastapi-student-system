from fastapi import FastAPI
from app.routes.students import router as students_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Management System API"}

app.include_router(students_router)