install:
	poetry install --no-root

requirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

run dev:
	uvicorn src.main:app --reload

db upgrade:
	alembic upgrade head

db downgrade:
	alembic downgrade -1

integration tests:
	pytest

unit tests:
	pytest