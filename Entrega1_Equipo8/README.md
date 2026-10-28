# Bebidas del Maipo S.A. — Entrega 1: Calidad y pronóstico

Caso integrador · Gestión de Producción de Bienes y Servicios (USACH) · Equipo 4

## Requisitos

- Python 3.10 o superior (probado con Python 3.13).
- Conexión a internet en la primera ejecución: los datos se descargan del repositorio docente en una
  revisión fija (`4f2718dc185dd3a5e94243424e386b558a460178`) y se verifica su huella SHA-256.
- No requiere GPU.

Instalar dependencias (versiones fijadas):

    python -m pip install -r requirements.txt

## Ejecución (un solo comando)

    python run.py

`run.py` borra las salidas de ejecuciones anteriores y ejecuta el notebook completo en una sesión limpia
(≈ 3 minutos). No se ingresan datos ni se modifican rutas. El orden interno es:

1. **Parte 1A — Control estadístico y capacidad de proceso** (cartas X̄–R, reglas Western Electric, estabilidad,
   Cp/Cpk/Pp/Ppk global y por turno, OIML R87, carta p, Pareto, sobrellenado).
2. **Parte 1B — Pronóstico de demanda** (diagnóstico de las 9 series, censura, ingenuo/ETS/SARIMA, validación por
   origen deslizante, BU/TD/MO, pronóstico a 13 semanas con intervalos 80/95 %).
3. **Parte 1C — Puente hacia la Entrega 2** (tabla de traspaso con ρℓ, sobrellenado, d̂ᵢₜ y σ̂ᵢ,ₕ).

1A y 1B son independientes entre sí; 1C reúne sus resultados y verifica que coincidan.

Alternativa sin terminal: abrir `Entrega1_final.ipynb` en Jupyter o Colab y usar **Ejecutar todo**
en una sesión nueva.

## Estructura

    .
    ├── README.md
    ├── requirements.txt
    ├── run.py                                    ← punto de entrada único
    ├── Entrega1_final.ipynb            ← código fuente (1A + 1B + 1C)
    ├── Entrega1_final_ejecutada.ipynb  ← generado por run.py, con todas las salidas
    ├── resultados/                               ← generado: Parte 1A
    │   ├── figuras/
    │   └── parte_1c/                             ← generado: Parte 1C
    │       └── traspaso_entrega2.csv             ← entrada literal de la Entrega 2
    └── salidas_avance1b/                         ← generado: Parte 1B
        ├── datos_crudos/                         ← copia inmutable de los CSV docentes
        ├── tablas/
        └── figuras/

Los datos crudos no se modifican: toda transformación ocurre en código y queda trazada en tablas.

## Tabla de traspaso a la Entrega 2

`resultados/parte_1c/traspaso_entrega2.csv` tiene una fila por SKU y semana del horizonte (9 × 13 = 117):

| Columna | Significado | Origen |
|---|---|---|
| `d_hat_cajas` | pronóstico puntual d̂ᵢₜ (cajas/semana) | 1B |
| `sigma_hat_cajas` | desviación estándar del error σ̂ᵢ,ₕ (cajas) | 1B, errores fuera de muestra del desarrollo |
| `lo80`, `hi80`, `lo95`, `hi95` | intervalos de predicción | 1B |
| `rho_linea`, `rho_linea_conservador` | tasa de merma efectiva ρℓ | 1A, carta p |
| `factor_produccion` | 1/(1 − ρℓ): cajas a producir por caja vendible | 1A |
| `sobrellenado_mL_bot` | sobrellenado medio por formato (mL/botella) | 1A, cartas X̄–R |
| `litros_jarabe_extra_por_caja` | jarabe adicional por caja producida | 1A |

Tablas compactas para el informe en la misma carpeta: `C1_rho_por_linea.csv`, `C2_sobrellenado_por_formato.csv`,
`C3_pronostico_dhat.csv`, `C4_sigma_error.csv`, `C5_sigma_error_acumulado_lead_time.csv`.

## Reproducibilidad

- Versiones fijadas en `requirements.txt`; el notebook registra las versiones activas en
  `salidas_avance1b/entorno_ejecucion.json`.
- Semillas explícitas (1A: 42; 1B: 20261014). El análisis es determinista.
- Verificaciones programadas al final de cada parte (no-leakage, límites de Fase I independientes de Fase II,
  selección y calibración firmadas antes de la prueba, coherencia de la tabla de traspaso). Si alguna falla,
  la ejecución se detiene con error.
- Toda cifra del informe se genera desde el código y queda guardada en `resultados/` o `salidas_avance1b/`.

## Comparación de las nueve series

En las figuras de ventas crudas, ventas frente a demanda estimada y pronóstico final, los nueve paneles comparten el mismo eje vertical dentro de cada figura. Se muestran las etiquetas en todos los paneles y se conservan los valores atípicos; la escala común puede hacer que las series de menor volumen se vean más planas. La corrección no modifica los datos ni los pronósticos.

La instantánea `Entrega1_final_ejecutada.ipynb` conservada en el repositorio corresponde a una ejecución anterior y puede mostrar gráficos con las escalas anteriores. Para obtener las figuras actualizadas, ejecuta de nuevo `Entrega1_final.ipynb` o `python run.py`.
