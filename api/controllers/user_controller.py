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

def user_get(id: int, db: Session = Depends(get_db)) -> Dict[str, Any]:
  user_repository = UserRepository(db)
  users = user_repository.get_by_id(id)

  return users

def user_create(payload: UserCreateDto, db: Session = Depends(get_db)) -> Dict[str, Any]:
  user_repository = UserRepository(db)

  data = payload.dict(exclude_unset = True)
  users = user_repository.create(data)

  return users

def user_update(id: int, payload: UserUpdateDto, db: Session = Depends(get_db)) -> Dict[str, Any]:
  user_repository = UserRepository(db)

  data = payload.dict(exclude_unset = True)
  users = user_repository.update(id, data)

  return users

def user_delete(id: int, db: Session = Depends(get_db)) -> Dict[str, Any]:
  user_repository = UserRepository(db)
  users = user_repository.delete(id)

  return users