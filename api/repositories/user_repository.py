from db.models import User
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
  def __init__(self, db):
    super().__init__(
      db,
      User,
      allowed = (
        User.id,
        User.username,
        User.email,
        User.contact,
        User.is_active
      )
    )