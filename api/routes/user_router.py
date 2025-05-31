from fastapi import APIRouter
from dto.user_dto import UserCreateDto, UserUpdateDto

from controllers.user_controller import (
  user_list,
  user_get,
  user_create,
  user_update,
  user_delete
)

router = APIRouter(prefix="/user")

router.add_api_route("/", endpoint=user_list, methods=["GET"])
router.add_api_route("/{id}", endpoint=user_get, methods=["GET"])
router.add_api_route("/", endpoint=user_create, methods=["POST"])
router.add_api_route("/{id}", endpoint=user_update, methods=["PUT"])
router.add_api_route("/{id}", endpoint=user_delete, methods=["DELETE"])