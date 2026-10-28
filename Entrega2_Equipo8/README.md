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
- **Planificación (2):** se crean automáticamente `Avance2_Equipo8_<identificador>/datos/crudos/` y `datos/heredados/`. La optimización usa esas entradas calculadas; los archivos del modelo, auditoría y escenarios se escriben en `Avance2_Equipo8_<identificador>/codigo/`.
- **Resultados:** `Avance2_Equipo8_<identificador>/resultados/` contiene las salidas y verificaciones generadas en la ejecución. Se registran hashes de los CSV y del traspaso.

**Nota académica:** el modelo de Entrega 2 mantiene decisiones y supuestos que deben verificarse frente al enunciado y rúbrica. El notebook fue revisado sintácticamente y se verificó la preparación automática con datos del caso, pero la corrida integral de todos los escenarios en un entorno Colab nuevo todavía no está certificada.

## Cambios de comparación y trazabilidad

Las tres figuras de nueve SKU (ventas crudas, demanda estimada y pronóstico) comparten el eje vertical dentro de cada figura. Los valores atípicos se mantienen; por ello, algunas series pequeñas pueden verse más planas.

El notebook conserva un único modelo de planificación: el avanzado. Comprueba los 10 archivos originales contra las huellas SHA-256 del commit docente fijado y crea una carpeta `Avance2_Equipo8_<identificador>/` nueva para cada ejecución, para no mezclar sus resultados con corridas previas. La ruta exacta se muestra al ejecutar y las salidas se pueden descargar desde el ZIP generado.
