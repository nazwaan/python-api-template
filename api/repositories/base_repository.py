from sqlalchemy.orm import Session

class BaseRepository:
  def __init__(self, db: Session, model, stmt):
    self.db = db
    self.model = model
    self.stmt = stmt

  def get_all(self):
    return self.db.execute(self.stmt).mappings().all()

  def commit(self):
    self.db.commit()

  def rollback(self):
    self.db.rollback()