from fastapi import Depends
from typing import List, Dict, Any
from sqlalchemy.orm import Session

from db.get_db import get_db
from repositories.user_repository import UserRepository
from dto.user_dto import UserCreateDto, UserUpdateDto

def user_list(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
  user_repository = UserRepository(db)
  users = user_repository.get_all()                                                                                                                                                                                                                                                                                                                                                                               

  return users

def user_get(id: int) -> dict:
  return {"message": f"Get user for id {id}"}

def user_create(data: UserCreateDto) -> dict:
  return {"message": f"User '{data.model_dump(exclude_unset=True)}' created."}

def user_update(id: int, data: UserUpdateDto) -> dict:
  return {"message": f"User '{id}' updated with '{data.model_dump(exclude_unset=True)}'"}

def user_delete(id: int) -> dict:
  return {"message": f"Delete user for id {id}"}