from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():
    return {"Hello": "Worlddddd"}



@app.get('/greet')
async def greet():
    return {"message": "Good day"}



# Working with Path parameters and optional query parameters
@app.get('/greet{name}')
async def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"Good day {name}, you are {age} years old" }





class Student(BaseModel):
    name: str
    age: int
    roll: int
    

@app.post('/create_student')
async def create_student(student_data: Student):
    return {
        "name": student_data.name,
        "age": student_data.age,
        "roll": student_data.roll
    }
    
    
    
    
@app.put('/update_student/{student_id}')
async def update_student(student_id: int, student_data: Student):
    return {
        "student_id": student_id,
        "name": student_data.name,
        "age": student_data.age,
        "roll": student_data.roll
    }