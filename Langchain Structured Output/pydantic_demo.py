from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str='Ishwar'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,description="Decimal value between 0 and 10")

new_student={'age':'25','email':'ishwar@example.com','cgpa':5}

student=Student(**new_student)

print(student)