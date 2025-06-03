from fastapi import Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from helpers.error_handler import error_handler
from db.get_db import get_db
from repositories.user_repository import UserRepository
from dto.user_dto import User, UserCreateDto, UserUpdateDto

def user_list(db: Session = Depends(get_db)) -> Optional[List[User]]:
  user_repository = UserRepository(db)

  try:
    users = user_repository.get_all()
  except Exception as e:
    error_handler(e, 500, "failed to fetch users")

  return users

def user_get(id: int, db: Session = Depends(get_db)) -> User:
  user_repository = UserRepository(db)

  try:
    users = user_repository.get_by_id(id)
  except Exception as e:
    error_handler(e, 500, "failed to fetch user")

  if users == None:
    error_handler(None, 404, "user not found")

  return users

def user_create(payload: UserCreateDto, db: Session = Depends(get_db)) -> User:
  user_repository = UserRepository(db)
  data = payload.dict(exclude_unset = True)

  try:
    users = user_repository.create(data)
  except Exception as e:
    error_handler(e, 500, "failed to create user")

  return users

def user_update(id: int, payload: UserUpdateDto, db: Session = Depends(get_db)) -> User:
  user_repository = UserRepository(db)
  data = payload.dict(exclude_unset = True)
  
  try:
    users = user_repository.update(id, data)
  except Exception as e:
    error_handler(e, 500, "failed to update user")

  if users == None:
    error_handler(None, 404, "user not found")

  return users

def user_delete(id: int, db: Session = Depends(get_db)) -> User:
  user_repository = UserRepository(db)

  try:
    users = user_repository.delete(id)
  except Exception as e:
    error_handler(e, 500, "failed to delete user")

  if users == None:
    error_handler(None, 404, "user not found")

  return users