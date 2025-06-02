from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

class BaseRepository:
  def __init__(self, db: Session, model, allowed):
    self.db = db
    self.model = model
    self.allowed = allowed

  def get_all(self):
    stmt = (
      select(*self.allowed)
    )

    return self.db.execute(stmt).mappings().all()
  
  def get_by_id(self, id: int):
    stmt = (
      select(*self.allowed)
      .where(self.model.id == id)
    )

    return self.db.execute(stmt).mappings().first()

  def create(self, data, commit: bool = True):
    stmt = (
      insert(self.model)
      .values(**data)
      .returning(*self.allowed)
    )

    result = self.db.execute(stmt)

    if(commit):
      self.db.commit()

    return result.mappings().first()

  def update(self, id, data, commit: bool = True):
    stmt = (
      update(self.model)
      .where(self.model.id == id)
      .values(**data)
      .returning(*self.allowed)
    )

    result = self.db.execute(stmt)

    if(commit):
      self.db.commit()

    return result.mappings().first()

  def delete(self, id, commit: bool = True):
    stmt = (
      delete(self.model)
      .where(self.model.id == id)
      .returning(*self.allowed)
    )

    result = self.db.execute(stmt)

    if(commit):
      self.db.commit()

    return result.mappings().first()