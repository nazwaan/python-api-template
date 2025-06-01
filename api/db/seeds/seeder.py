from api.db.session import SessionLocal
from api.db.seeds.user_seeds import users

def seeder():
  db = SessionLocal()
  print("connected for seeding")

  try:
    print("seeding...")
    db.add_all(users)

    db.commit()
    print("seeding completed")
  finally:
    db.close()

seeder()