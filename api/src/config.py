import os

DB_USERNAME = os.getenv('DB_USERNAME') or 'postgres'
DB_PASSWORD = os.getenv('DB_PASSWORD') or 'postgres'
DB_HOST = os.getenv('DB_HOST') or 'localhost'
DB_PORT = os.getenv('DB_PORT') or 5432
DB_NAME = os.getenv('DB_NAME') or 'creditcard'
SECRET_KEY_CRIPTO = 'ff90e20a-8117-463c-9210-aa3031c8c731'
