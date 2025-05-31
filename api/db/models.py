from sqlalchemy import Column, Integer, String, Boolean
from .session import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True, nullable=False)
  email = Column(String, unique=True, index=True, nullable=False)
  contact = Column(String, nullable=True)
  is_active = Column(Boolean, default=True, nullable=False)