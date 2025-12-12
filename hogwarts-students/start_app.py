"""start_app.py
Helper to start the Flask app using the project's virtualenv Python on Windows.

Usage (PowerShell):
  python start_app.py

This locates `.venv\Scripts\python.exe` and runs `.venv\app.py` with the current
environment (it will load `.env` automatically because the app uses python-dotenv).

If you prefer, run the venv python directly:
  & ".\\.venv\\Scripts\\python.exe" ".\\.venv\\app.py"
"""
import os
import subprocess
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
VENV_PY = os.path.join(HERE, ".venv", "Scripts", "python.exe")
APP_PY = os.path.join(HERE, ".venv", "app.py")

if not os.path.exists(VENV_PY):
    print("Virtualenv Python not found at:", VENV_PY)
    print("You can run the app with your Python, or create a virtualenv at .venv and install requirements.")
    sys.exit(1)

if not os.path.exists(APP_PY):
    print("app.py not found at expected location:", APP_PY)
    sys.exit(1)

print("Starting Flask app using:", VENV_PY)
proc = subprocess.Popen([VENV_PY, APP_PY], env=os.environ)
try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
