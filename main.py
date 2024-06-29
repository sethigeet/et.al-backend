import os
from dotenv import load_dotenv

env = "development" if os.environ.get("PYTHON_ENV") is None else "production"
load_dotenv(f".env.{env}")

