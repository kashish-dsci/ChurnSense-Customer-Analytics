
import subprocess
import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent
dashboard_file = project_folder / "dashboard.py"

subprocess.run([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(dashboard_file)
], cwd=str(project_folder))
