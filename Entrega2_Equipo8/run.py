"""Ejecución reproducible del CaseStudy Equipo 8: python run.py.
Sin subir ZIP ni CSV: el notebook clona los datos del profesor y calcula 1A/1B/1C.
"""
from pathlib import Path
import subprocess
import sys

DIR = Path(__file__).resolve().parent
NOTEBOOK = DIR / "Entrega2_Equipo8.ipynb"
if not NOTEBOOK.is_file():
    raise FileNotFoundError(f"No se encontró {NOTEBOOK}")

try:
    import nbconvert
    import ipykernel
except ImportError:
    subprocess.run([
        sys.executable, "-m", "pip", "install", "-q",
        "nbconvert==7.16.6", "ipykernel==6.29.5"
    ], check=True)

cmd = [
    sys.executable, "-m", "nbconvert",
    "--to", "notebook", "--execute",
    "--ExecutePreprocessor.timeout=3600",
    "--output", "Entrega2_Equipo8_ejecutada.ipynb",
    str(NOTEBOOK),
]
print("Ejecutando Entrega 1 y Entrega 2 sin cargas manuales...", flush=True)
subprocess.run(cmd, cwd=DIR, check=True)
print("Revisar Entrega2_Equipo8_ejecutada.ipynb y la ruta de resultados indicada en el notebook.", flush=True)
