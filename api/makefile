install:
	poetry install --no-root

requirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

run dev:
	uvicorn src.main:app --reload