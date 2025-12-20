import os
import sys
from typing import Union

def load_project_env(filename: str = ".env") -> Union[None, str]:
    current_path = os.getcwd()
    
    while True:
        env_file = os.path.join(current_path, filename)
        if os.path.isfile(env_file):
            load_dotenv(env_file)
            return env_file
        
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            raise FileNotFoundError(f"{filename} not found starting from {os.getcwd()}")
        
        current_path = parent_path



def load_dotenv(env_file):
    with open(env_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                os.environ[key] = value