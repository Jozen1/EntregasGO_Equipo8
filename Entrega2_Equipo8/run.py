"""Ejecutar desde la raíz: python Entrega2_Equipo8/run.py."""
from pathlib import Path
import json,os,subprocess,sys
root=Path(__file__).resolve().parent
subprocess.run([sys.executable,'-m','pip','install','-q','-r',str(root/'requirements.txt')],check=True)
from IPython.core.interactiveshell import InteractiveShell
os.chdir(root)
notebook=json.loads((root/'Entrega2_Equipo8.ipynb').read_text(encoding='utf-8'))
shell=InteractiveShell.instance()
for index,cell in enumerate(notebook['cells']):
    if cell['cell_type']!='code':continue
    print(f'Celda {index+1}/{len(notebook["cells"])}',flush=True)
    result=shell.run_cell(''.join(cell['source']),store_history=False)
    error=result.error_before_exec or result.error_in_exec
    if error:raise RuntimeError(f'Falló la celda {index+1}') from error
print('Ejecución completa. Salidas en Avance2_Equipo8/resultados/.')
