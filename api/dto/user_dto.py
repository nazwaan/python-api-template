from pydantic import BaseModel, Field
from typing import TypedDict, Annotated

# optional and nullable:         Annotated[str | None, Field(default=None)]
# required but nullable:         Annotated[str | None, Field()]
# optional but not nullable:     Annotated[str, Field(default=None)]

class User(TypedDict):
  id: int
  username: str
  email: str
  contact: str | None
  is_active: bool

class UserCreateDto(BaseModel):
  username: str
  email: str
  contact: Annotated[str | None, Field(default=None)]

class UserUpdateDto(BaseModel):
  username: Annotated[str, Field(default=None)]
  email: Annotated[str, Field(default=None)]
  contact: Annotated[str | None, Field(default=None)]
  is_active: Annotated[bool, Field(default=None)]