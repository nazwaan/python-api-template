from api.db.models import User

users = [
  User(username="admin", email="admin@example.com", contact="7777777", is_active=True),
  User(username="john", email="johndoe@example.com", contact="7777781", is_active=True),
  User(username="testuser", email="testuser@example.com", contact="7777778", is_active=True),
  User(username="testuser2", email="testuser2@example.com", contact="7777779", is_active=True)
]