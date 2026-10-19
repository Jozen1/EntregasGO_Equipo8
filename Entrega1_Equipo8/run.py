"""Punto de entrada único de la Entrega 1 (Partes 1A, 1B y 1C).

Uso, desde la raíz del repositorio:
    python -m pip install -r requirements.txt   # una vez
    python run.py

Borra las salidas de ejecuciones anteriores y ejecuta el notebook completo en una sesión limpia.
El notebook ejecutado (con todas sus salidas) queda en Entrega1_final_ejecutada.ipynb.
"""
from pathlib import Path
import shutil
import subprocess
import sys
import time

RAIZ = Path(__file__).resolve().parent
NOTEBOOK = RAIZ / "Entrega1_final.ipynb"
SALIDA = RAIZ / "Entrega1_final_ejecutada.ipynb"
GENERADOS = [RAIZ / "resultados", RAIZ / "salidas_avance1b", RAIZ / "Resultados_Avance1B.zip", SALIDA]


def main() -> None:
    if sys.version_info < (3, 10):
        sys.exit("Se requiere Python 3.10 o superior.")
    if not NOTEBOOK.exists():
        sys.exit(f"No existe {NOTEBOOK.name}")

    # Ejecución limpia: ninguna salida previa puede influir en los resultados.
    for ruta in GENERADOS:
        if ruta.is_dir():
            shutil.rmtree(ruta)
        elif ruta.exists():
            ruta.unlink()

    print("Ejecutando Entrega 1 (1A → 1B → 1C)...", flush=True)
    inicio = time.time()
    subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
         str(NOTEBOOK), "--output", SALIDA.name, "--output-dir", str(RAIZ),
         "--ExecutePreprocessor.timeout=-1", "--ExecutePreprocessor.kernel_name=python3"],
        check=True, cwd=RAIZ,
    )
    minutos = (time.time() - inicio) / 60
    print(f"\nEntrega 1 ejecutada correctamente en {minutos:.1f} min.")
    print(f"Notebook ejecutado : {SALIDA.name}")
    print("Resultados 1A      : resultados/")
    print("Resultados 1B      : salidas_avance1b/")
    print("Tabla para E2 (1C) : resultados/parte_1c/traspaso_entrega2.csv")


if __name__ == "__main__":
    main()
