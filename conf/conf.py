import os
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(__file__), f".{os.getenv('ENV')}.env")
secrets_path = os.path.join(os.path.dirname(__file__), "secrets", "secrets.env")
load_dotenv(env_path)
load_dotenv(secrets_path)


class SecData:
    BASE_URL = os.getenv("BASE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
