import os
import re
from utils import env


PROJECT_ROOT_KEY = "PROJECT_ROOT"


try:
    env.load_project_env()
except FileNotFoundError:
    print(f"Environment file not found, new project root: {os.getcwd()}")
    os.environ[PROJECT_ROOT_KEY] = os.getcwd()


VAULT_ROOT = os.getenv(PROJECT_ROOT_KEY)
