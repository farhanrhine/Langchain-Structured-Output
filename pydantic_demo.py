from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'farhan'
    age: Optional[int] = None
    email: EmailStr = None
    cgpa: float = Field(gt=0, lt=10, default=6, description='A decimal value representing the cgpa of the student')


new_student = {'age':'23', 'email':'mohammadfarhanalam09@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['name'])

student_json = student.model_dump_json()