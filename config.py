from dotenv import load_dotenv
import os

load_dotenv('.env')

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


DATABASE_URL = f"postgresql://neondb_owner:npg_C51ThWmdjlqE@ep-aged-snowflake-a57llk4f-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"




