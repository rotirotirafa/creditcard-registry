import os

DB_USERNAME = os.getenv('DB_USERNAME') or 'postgres'
DB_PASSWORD = os.getenv('DB_PASSWORD') or 'postgres'
DB_HOST = os.getenv('DB_HOST') or 'localhost'
DB_PORT = os.getenv('DB_PORT') or 5432
DB_NAME = os.getenv('DB_NAME') or 'creditcard'
SECRET_KEY = "segredo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
