from fastapi import APIRouter, HTTPException
from app.db import get_db
from app.models import Student

router = APIRouter(prefix="/students", tags=["students"])

@router.get('')
def all_students():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("select name, age, marks, result from students order by id asc")
        students = cursor.fetchall()

        return {"Students": students}
    
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()


@router.get("/{student_id}")
def get_students(student_id: int):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        student = cursor.fetchone()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        return student

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@router.post('')
def create_student(student:Student):
    try:
        db = get_db()
        cursor = db.cursor()
        result = "Pass" if student.marks>40 else "Fail"
        sql = "INSERT INTO STUDENTS (name, age, marks, result) VALUES (%s, %s, %s, %s)"
        values = (student.name, student.age, student.marks, result)
        cursor.execute(sql, values)
        db.commit()
        return {
            "message": "Student Created",
            "data": {
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
                "result": result
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()
    

@router.put("/{student_id}")
def update_student(student_id:int ,student:Student):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        if student.age<0:
            raise HTTPException(status_code=400, detail="Age can't be negative")
        
        if 0>student.marks or student.marks>100:
            raise HTTPException(status_code=400, detail="Enter valid marks between 1 to 100")
        
        result = "Pass" if student.marks>40 else "Fail"
        cursor.execute("update students set name=%s, age=%s, marks=%s, result=%s where id=%s",
                       (student.name, student.age, student.marks, result, student_id))
        db.commit()

        if cursor.rowcount==0:
            raise HTTPException(status_code=404, detail='Student Not Found')

        return{
            "message": "Student Updated",
            "data":{
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
                "result": result
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()

    
@router.delete("/{student_id}")
def delete_students(student_id: int):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student id not in the DB")

        return {
            "message": f"Student deleted with id {student_id}"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()
