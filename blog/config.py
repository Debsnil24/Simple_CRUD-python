import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("DB URL is not set. Check your .env file")