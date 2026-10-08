from fastapi import APIRouter, Depends
from app.auth import verify_api_key
from app.jwt_auth import verify_jwt
from pydantic import BaseModel

router = APIRouter()


class Student(BaseModel):
    name: str
    age: int
    course: str


students = []


# GET all students - JWT protected
@router.get("/", dependencies=[Depends(verify_jwt)])
def get_students():
    return {
        "students": students
    }


# POST student - API key protected
@router.post("/", dependencies=[Depends(verify_api_key)])
def add_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    return {
        "message": "Student added successfully",
        "student": new_student
    }


# GET student by ID
@router.get("/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {
        "message": "Student not found"
    }


# UPDATE student
@router.put("/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    course: str
):
    for student in students:
        if student["id"] == student_id:
            student["name"] = name
            student["age"] = age
            student["course"] = course

            return {
                "message": "Student updated successfully",
                "student": student
            }

    return {
        "message": "Student not found"
    }


# DELETE student
@router.delete("/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    return {
        "message": "Student not found"
    }