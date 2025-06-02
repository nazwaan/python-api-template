from sqlalchemy import select
from db.models import User
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
  def __init__(self, db):
    super().__init__(
      db,
      User,
      stmt = select(
        User.id,
        User.username,
        User.email,
        User.contact,
        User.is_active
      )
    )