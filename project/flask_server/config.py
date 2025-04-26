import os

from flask.cli import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")
DATABASE_PATH = os.getenv("DATABASE_PATH")
SQL_SCRIPT_PATH = os.getenv("SQL_SCRIPT_PATH")