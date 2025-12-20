import os
import sys
import subprocess
import argparse
import venv
import platform

from utils.constants import PROJECT_ROOT_KEY

VENV_DIR = ".venv"
REQUIREMENTS_FILE = "requirements.txt"


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, VENV_DIR)
REQUIREMENTS_FILE = os.path.join(SCRIPT_DIR, REQUIREMENTS_FILE)   

def check_virtualenv(venv_dir):
    if os.path.isdir(venv_dir):
        print(f"Virtual environment already exists in `{venv_dir}`")
        return True
    return False
    
def print_activation_instructions(venv_dir):
    print("\nSetup completed.")
    print("To activate the environment manually:\n")
    if os.name == 'nt':
        print(f"  {venv_dir}\\Scripts\\activate.bat")
    else:
        print(f"  source {venv_dir}/bin/activate")
    print()

def create_virtualenv():
    print("Creating virtual environment...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(VENV_DIR)
    
def add_project_root_to_venv():
    print("Adding project root path to `.env` file...")
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(f"{PROJECT_ROOT_KEY}={SCRIPT_DIR}")
    else:
        with open('.env', 'r') as f:
            env_variables = f.read()
        
        lines_post = []
        for line in env_variables.split("\n"):
            key, value = line.split("=")
            if key == PROJECT_ROOT_KEY:
                lines_post.append("=".join([key, SCRIPT_DIR]))
            else:
                lines_post.append("=".join([key, value]))
        
        env_post = "\n".join(lines_post)
        
        with open('.env', 'w') as f:
            f.write(env_post)
            
def get_pip_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, "Scripts", "pip.exe").replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, "bin", "pip")

def get_activate_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'activate.bat').replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, 'bin', 'activate')
    
    
def get_python_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'python.exe').replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, 'bin', 'python')

def install_requirements():
    pip_path = get_pip_path()

    if not os.path.isfile(REQUIREMENTS_FILE):
        print(f"Error: {REQUIREMENTS_FILE} not found in {SCRIPT_DIR}")
        sys.exit(1)

    print(f"Installing packages from {REQUIREMENTS_FILE}...")
    subprocess.check_call([pip_path, "install", "-r", REQUIREMENTS_FILE])
   

    
def main():
    parser = argparse.ArgumentParser(
        prog='Environment Setup',
        description='Setup virtual environment',#and install filters.',
        add_help=True)
    
    args = parser.parse_args()
    
    try:
        if not check_virtualenv(VENV_DIR):
            create_virtualenv()
            add_project_root_to_venv()
            
        install_requirements()
        print_activation_instructions(VENV_DIR)
    except Exception as e:
        print(f"Error during setup: {e}", file=sys.stderr)
        sys.exit(1)

    if sys.stdin.isatty():
        input("Press ENTER to quit.")

if __name__ == "__main__":
    main()