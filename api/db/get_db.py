from sqlalchemy import text
from sqlalchemy.orm import Session
from db.session import SessionLocal
from helpers.error_handler import error_handler

def get_db():
  try:
    db: Session = SessionLocal()
    db.execute(text("SELECT 1"))
  except Exception as e:
    error_handler(e, 500, "failed to establish a connection to the database")
  
  try:
    yield db
  finally:
    db.close()