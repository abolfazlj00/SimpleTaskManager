from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_ECHO = (os.getenv("DATABASE_ECHO") or "false").lower() == "true"