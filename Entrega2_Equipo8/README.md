# Entrega 2 — Bebidas del Maipo S.A. · Equipo 8

Notebook reproducible de calidad, pronóstico y planificación de producción e inventario. **No requiere subir ZIP ni CSV ni montar Google Drive.**

## Ejecutar en Google Colab

Abrir [Entrega2_Equipo8.ipynb](Entrega2_Equipo8.ipynb) con Google Colab. En una sesión nueva, seleccionar **Entorno de ejecución → Ejecutar todo**. Requiere internet para instalar paquetes y obtener los datos oficiales.

## Ejecutar desde GitHub (Python)

Clonar el repositorio y entrar a esta carpeta, luego:

```bash
python run.py
```

El ejecutor instala Jupyter si hace falta y ejecuta el notebook completo, dejando `Entrega2_Equipo8_ejecutada.ipynb`. Se necesita Python 3.11 o superior, Git instalado e internet en la primera ejecución.

## Flujo y reproducibilidad

- **Datos oficiales:** se obtienen desde `LuisRojo-Gonzalez/Operations-Management`, `CaseStudy/Datos`, con commit congelado `4f2718dc185dd3a5e94243424e386b558a460178`. Se reutilizan los nueve CSV originales sin transformarlos.
- **Calidad (1A) y pronóstico (1B):** se ejecutan en el notebook. El puente 1C produce `entrada_e2` (117 filas, 9 SKU × 13 semanas) y `sigma_acum`.
- **Planificación (2):** se crean automáticamente `Avance2_Equipo8/datos/crudos/` y `datos/heredados/`. La optimización usa esas entradas calculadas; los archivos del modelo, auditoría y escenarios se escriben en `Avance2_Equipo8/codigo/`.
- **Resultados:** `Avance2_Equipo8/resultados/` contiene las salidas y verificaciones generadas en la ejecución. Se registran hashes de los CSV y del traspaso.

**Nota académica:** el modelo de Entrega 2 mantiene decisiones y supuestos que deben verificarse frente al enunciado y rúbrica. El notebook fue revisado sintácticamente y se verificó la preparación automática con datos del caso, pero la corrida integral de todos los escenarios en un entorno Colab nuevo todavía no está certificada.
