from typing import Annotated, Optional
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=50)]
    age: Annotated[int, Field(gt=0, lt=120)]
    marks: Annotated[int, Field(gt=0, lt=100)]