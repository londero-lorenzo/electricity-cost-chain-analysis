import os
import argparse
import platform
import subprocess
import sys
from setup import VENV_DIR
from setup import get_activate_path
from typing import Union

def open_venv_shell(alternative_command= ""):
    activate_path = get_activate_path()
    
    if os.name == 'nt':
        cmd = f'cmd.exe /k "{activate_path} && '
        if alternative_command:
            cmd += alternative_command
        else:
            cmd += 'echo Environment activated. Type `exit` to exit.'
        cmd += '"'
        subprocess.run(cmd)
    else:
        shell = os.environ.get('SHELL', '/bin/bash')
        cmd = f'{shell} -c "source {activate_path}; '
        if alternative_command:
            cmd += alternative_command + '; '
        else:
            cmd += 'echo Environment activated. Type `exit` to exit.; '
        cmd += f'exec {shell}"'
        subprocess.run(cmd)
        

def run_jupyter(mode: str, port: Union[int, None]= None, no_browser: bool= False):
    if mode not in ("lab", "notebook"):
        print(f"[ERROR] Unknown jupyter mode: {mode}")
        sys.exit(1)

    cmd = ["jupyter", mode]

    if port:
        cmd += ["--port", str(port)]

    if no_browser:
        cmd.append("--no-browser")

    print("[INFO] Starting:", " ".join(cmd))
    open_venv_shell(" ".join(cmd))


def main():
    parser = argparse.ArgumentParser(
        prog="Environment starter",
        description="Start a virtual environment shell or Jupyter inside the venv",
        epilog="Run without arguments to open an interactive shell."
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---- jupyter ----
    jupyter_parser = subparsers.add_parser(
        "jupyter",
        help="Start Jupyter Lab or Notebook inside the venv"
    )
    jupyter_parser.add_argument(
        "mode",
        choices=["lab", "notebook"]
    )
    jupyter_parser.add_argument("--port", type=int)
    jupyter_parser.add_argument("--no-browser", action="store_true")

    args = parser.parse_args()

    # ---- DEFAULT: shell ----
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        exit(0) 
            
    if args.command is None:
        open_venv_shell()
        return

    if args.command == "jupyter":
        run_jupyter(args.mode, args.port, args.no_browser)

if __name__ == "__main__":
    main()