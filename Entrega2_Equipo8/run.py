"""Ejecutar desde la raíz con python Entrega2_Equipo8/run.py."""
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", str(root / "requirements.txt")],
    check=True,
)

from IPython.core.interactiveshell import InteractiveShell

os.environ["BDM_E2_DEPENDENCIAS_INSTALADAS"] = "1"
os.environ.setdefault("DATOS_DIR", str(root.parent / "datos" / "crudos"))
os.chdir(root)
notebook = json.loads((root / "Entrega2_Equipo8.ipynb").read_text(encoding="utf-8"))
shell = InteractiveShell.instance()
for index, cell in enumerate(notebook["cells"], start=1):
    if cell["cell_type"] != "code":
        continue
    print(f"Celda {index}/{len(notebook['cells'])}", flush=True)
    result = shell.run_cell("".join(cell["source"]), store_history=False)
    error = result.error_before_exec or result.error_in_exec
    if error:
        raise RuntimeError(f"Falló la celda {index}") from error

print(f"Ejecución completa. Salidas en {root / 'Avance2_Equipo8' / 'resultados'}.")
