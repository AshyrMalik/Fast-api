import enum
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, enum.Enum):
    male = "male"
    female = "female"


class Roles(str, enum.Enum):
    admin = "admin"
    student = "student"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Roles]
