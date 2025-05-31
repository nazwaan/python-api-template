from fastapi import APIRouter
from dto.user_dto import UserCreateDto, UserUpdateDto
import json

router = APIRouter(prefix="/user")

def user_list():
  return { "message": "list all user" }

def user_get(id: int):
  return { "message": f"Get user for id {id}" }

def user_create(data: UserCreateDto):
  return {
    "message": f"User '{data.model_dump(exclude_unset=True)}' created."
  }

def user_update(id: int, data: UserUpdateDto):
  return {
    "message": f"User '{id}' updated with '{data.model_dump(exclude_unset=True)}'"
  }

def user_delete(id: int):
  return { "message": f"Delete user for id {id}" }

router.add_api_route("/", endpoint=user_list, methods=["GET"])
router.add_api_route("/{id}", endpoint=user_get, methods=["GET"])
router.add_api_route("/", endpoint=user_create, methods=["POST"])
router.add_api_route("/{id}", endpoint=user_update, methods=["PUT"])
router.add_api_route("/{id}", endpoint=user_delete, methods=["DELETE"])