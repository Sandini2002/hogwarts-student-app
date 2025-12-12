# Hogwarts Students — How to run

1. & ".\.venv\Scripts\pip.exe" install -r requirements.txt
2. python start_app.py

This project runs a small Flask app. Below are quick steps to run it on Windows with the included `.venv`.

Prerequisites
- Python 3.10+ installed (system-wide) — the repository contains a virtualenv at `.venv`.

Quick start (PowerShell)

1. Ensure the virtualenv exists at `.venv` and required packages are installed.
   If you haven't installed dependencies yet, run:

```powershell
& ".\.venv\Scripts\pip.exe" install -r requirements.txt
```

2. (Optional) Set the `DATABASE_URL` to point to Postgres (if you want to use Postgres instead of the default SQLite):

```powershell
#$env:DATABASE_URL = 'postgresql://user:pass@host:5432/hogwarts_db'
```

3. Start the app using the helper script (this invokes the venv Python and runs the app file):

```powershell
python start_app.py
```

Or run the venv python directly:

```powershell
& ".\.venv\Scripts\python.exe" ".\.venv\app.py"
```

Then open http://127.0.0.1:5000 in your browser.

Notes
- Templates live in `.venv/templates` (this project currently keeps app files inside the venv). It's recommended to move `app.py`, `templates/` and `static/` to the repo root for clarity — I can help with that.
- To use Postgres, install a DB driver in the venv, e.g.:

```powershell
& ".\.venv\Scripts\pip.exe" install psycopg2-binary
```

If you want, I can create a `scripts/` folder with a PowerShell setup script to recreate the venv and install dependencies.