install:
	pip install -r requirements.txt

api-dev: 
	python api/main.py

migrate-make:
	@alembic revision --autogenerate -m "$(name)"

migrate-latest:
	alembic upgrade head

migrate-refresh:
	alembic downgrade base
	alembic upgrade head
	python -m api.db.seeds.seeder

seed:
	python -m api.db.seeds.seeder