from dto.user_dto import UserCreateDto, UserUpdateDto

def user_list() -> dict:
  return {"message": "list all user"}

def user_get(id: int) -> dict:
  return {"message": f"Get user for id {id}"}

def user_create(data: UserCreateDto) -> dict:
  return {"message": f"User '{data.model_dump(exclude_unset=True)}' created."}

def user_update(id: int, data: UserUpdateDto) -> dict:
  return {"message": f"User '{id}' updated with '{data.model_dump(exclude_unset=True)}'"}

def user_delete(id: int) -> dict:
  return {"message": f"Delete user for id {id}"}