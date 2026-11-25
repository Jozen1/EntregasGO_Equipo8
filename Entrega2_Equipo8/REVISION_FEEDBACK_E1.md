# Entrega 2 del Equipo 8 · Revisión del feedback de la Entrega 1

Se contrastó el informe docente «Retroalimentación del caso integrador — Entrega 1», §§4–7, con la versión de Entrega 2 en [`4b05c62`](https://github.com/Jozen1/EntregasGO_Equipo8/tree/4b05c6218fbcbc46426ecc75556459c3eb5fedb4/Entrega2_Equipo8). Esta nota documenta hallazgos y propone correcciones. Las cifras de planificación corresponden al plan publicado. Para esta revisión se comprobaron salidas y se recalcularon comparaciones puntuales, sin una nueva optimización.

## Las cinco correcciones priorizadas por el profesor

| Observación del correo (§5) | Estado en Entrega 2 | Evidencia y trabajo pendiente |
|---|---|---|
| 1. Separar estabilidad por 3σ y por reglas Western Electric (WE) | Parcial | En 1A §3.1 se cuentan ambos tipos de señal, pero solo se emite un dictamen, `estable`, basado en 3σ. Las conclusiones de capacidad heredan ese dictamen. |
| 2. Auditar las 16 exclusiones del turno C | Parcial | En 1A §2 se registran identificador, fecha, hora, turno, SKU, media y rango. Se retiraron 11 subgrupos de 1,5 L y 5 de 3 L. La pertenencia al turno C es la justificación operativa usada por el algoritmo. Falta evidencia física individual y una comparación explícita conservando los 16. |
| 3. Verificar cobertura y amplitud por SKU y horizonte antes de elegir el stock de seguridad | Parcial | En 1B §§10–11 la desviación se estima por nodo y horizonte. La **evaluación** de bandas se publica por nodo y por nivel × horizonte, separadamente. La E2 usa una normal centrada con la desviación del desarrollo. Falta el diagnóstico conjunto por SKU × horizonte, contrastar la cola superior y justificar la protección que llega al plan. |
| 4. Unificar notebook y versión de Python | Resuelto para E2 | El [README](README.md) y [run.py](run.py) apuntan a `Entrega2_Equipo8.ipynb`. El README indica Python 3.11+ y la [corrida archivada](resultados_verificados/entorno.json) registra Python 3.12.14 y NumPy 2.3.5. La verificación aquí se refiere a la documentación y la ejecución archivada de E2. |
| 5. Mantener ambas hipótesis de unidad y contrastar con el ERP | Sensibilidad aplicada, comprobación de origen pendiente | En 1B §§4, 13 y 14 se separan ventas observadas y transformadas y se recalcula el pronóstico con y sin ajuste. La base activa el ajuste. No se identificó documentación original que confirme el error en CIT-L05, semana 118, o NEC-D15, semana 63. |

## Cómo cerrar las tres observaciones mayores

### 1. Mostrar exactamente qué criterio pasa cada turno

Añadir a la tabla de estabilidad las columnas «subgrupos con señal 3σ en X̄ o R», «subgrupos con señal WE1–WE4 en X̄ o fuera de límites en R», y un dictamen para cada criterio. Contar subgrupos únicos mediante la unión de señales. Conservar alcance, semanas, turno y origen de los límites.

| Resultados publicados | Criterio 3σ | Reglas completas |
|---|---:|---:|
| L2, 1,5 L, turno B, límites del propio tramo | 0 subgrupos con señal | 3 con señal |
| L2, 1,5 L, turno C, límites del propio tramo | 0 subgrupos con señal | 3 con señal |
| L1, 0,5 L, Fase II, límites congelados de Fase I | 91 de 120 | 120 de 120 |

Texto propuesto para el informe: «En L2, 1,5 L, los turnos B y C tuvieron cero puntos fuera de los límites de 3σ y tres señales Western Electric cada uno. Los índices Cp y Cpk describen los tramos observados. Para proyectar su capacidad se requiere observar períodos posteriores con límites congelados». Usar la misma distinción en los títulos de las figuras y las conclusiones.

### 2. Mantener una referencia con los 16 subgrupos

Usar los datos completos como referencia mientras se verifica la causa. Conservar la depuración actual como escenario comparativo. Para cada ID registrar «causa verificada», «hipótesis sin verificar» o «sin antecedente», con referencia al registro de ajuste, mantención o incidente si existe. Si la fuente no está disponible, conservar esa condición en la tabla. Comparar límites X̄–R y volver a contar señales sobre las **mismas observaciones** de monitoreo.

| L2, Fase I semanas 1–8 | Límites de X̄ con todos los datos (mL) | Límites publicados con depuración (mL) |
|---|---:|---:|
| 1,5 L | 1.497,79 a 1.511,53 | 1.497,81 a 1.510,96 |
| 3,0 L | 2.996,98 a 3.020,12 | 2.997,05 a 3.019,83 |

La primera columna numérica se recalculó con el CSV oficial de llenado, subgrupos de cinco y la misma constante A2 = 0,577 del cuaderno. Revisar qué cambia en la interpretación. La merma del plan procede de la carta de atributos y el sobrellenado utiliza datos de volumen. Una diferencia en los límites de X̄ no implica por sí sola una diferencia en esos parámetros.

### 3. Calibrar la protección que consume el plan

1. En las predicciones externas ya generadas, mostrar una fila por SKU y horizonte con número de orígenes evaluables, cobertura y ancho medio en cajas de las bandas del 80 % y 95 %. Añadir la proporción de errores que excede el stock de seguridad propuesto. Hay ocho orígenes externos por combinación y las ventanas se superponen. Un acierto adicional cambia la cobertura observada en 12,5 puntos porcentuales.
2. Como diagnóstico, la banda nominal del 80 % cubre 92,63 % en SKU y 93,27 % en planta. Al cruzar los errores guardados, NEC-D05 cubre 5 de 8 observaciones en h=2 y h=3 (62,5 %, anchos medios de 580 y 574 cajas), y 8 de 8 en h=7. Se verificó que los agregados de cobertura y amplitud de la tabla de predicciones reproducen las salidas archivadas por nodo. Esto justifica examinar el cruce antes de aplicar un factor común.
3. Con la fórmula actual como referencia, comparar una alternativa que estime el cuantil superior de demanda real menos pronóstico, al nivel de servicio de cada SKU. Separar la estimación y evaluación cronológicamente dentro del desarrollo y usar únicamente errores cuyo resultado ya se conocía en cada corte. Con pocos orígenes, predefinir agrupaciones de horizontes cercanos o compartir información entre SKU comparables. Conservar las bandas bilaterales para comunicar incertidumbre. Para el stock, contrastar específicamente la protección **unilateral**.
4. Documentar el criterio de elección usando desempeño en desarrollo, cobertura y ancho. La prueba externa ya fue inspeccionada: conservarla como diagnóstico y explicitar esta limitación al evaluar un método nuevo. Si el método actual se sostiene, justificarlo. Si cambia el stock, recalcular el escenario y contrastar costo, inventario, déficit de seguridad, atraso y compromisos de semana 12 con el plan publicado.

## Otros comentarios del correo (§§4 y 6)

| Tema | Qué está comprobado | Propuesta |
|---|---|---|
| Ventanas de Fase I | El algoritmo busca un cambio en las semanas 1–8, con umbral de dos desviaciones de X̄. En L1 fija el corte en 5 y luego etiqueta 6–10 como monitoreo. Las semanas 6–8 influyen en la elección del corte. | Describir 1–8 como diagnóstico retrospectivo, congelar la referencia y mostrar 9–10 como monitoreo posterior común a las líneas. Contrastar las referencias 1–5 y 1–8 sobre las mismas semanas 9–10. Como comprobación, en L1 los límites de X̄ pasan de 499,66–505,27 a 500,91–506,50 mL al extender la ventana. |
| Merma, sobrellenado e impacto económico | En L2 el factor de producción pasa de 1,0267 sin el episodio extraordinario a 1,0321 con él. Existe un escenario de merma conservadora. Se calcula sobrellenado por turno, pero el plan usa una media por formato. | Presentar ambos factores como cajas brutas por caja vendible. Probar cómo una mezcla de turnos observada con mayor sobrellenado afecta litros de jarabe, costo y factibilidad, manteniendo lo demás fijo. |
| Pareto | Cada inspección tiene una causa principal. El código atribuye a esa causa todas sus unidades defectuosas. | Rotular el gráfico «Unidades defectuosas agrupadas por causa principal de la inspección». Aclarar que el dato identifica la causa principal del registro y no identifica la causa de cada botella. |
| Anomalías del ERP | Sin ajustar por unidad, el total pronosticado de 13 semanas aumenta 22,68 % para CIT-L05 y 12,22 % para NEC-D15 frente a la base. | Añadir una tabla con registro original, unidad declarada, hipótesis y efecto. Solicitar la orden o movimiento fuente de esas dos semanas si está disponible. Hasta entonces, declarar el ajuste como supuesto y preservar la sensibilidad. |
| Separación temporal y tamaño muestral | Hay 20 orígenes de desarrollo y 8 externos. La selección y la calibración quedan congeladas antes de las semanas objetivo de prueba (137–156). El cuaderno reporta pares y orígenes por horizonte. | Conservar los controles y situar el denominador junto a cada nueva tabla de cobertura. |
| Traspaso y correspondencia | El [CSV usado en E2](resultados_verificados/traspaso/traspaso_entrega2.csv) tiene 117 pares SKU–semana únicos y suma 174.382,875 cajas, que redondean a 174.383. El cuaderno verifica sumas semanales por familia y planta y correspondencia de parámetros de calidad y pronóstico. | Mantener estas pruebas si se adopta una recalibración y distinguir la versión original del traspaso revisado. |

La escala común de los nueve gráficos, comentada por el equipo en otra ocasión, ya está aplicada dentro de cada figura de ventas, demanda reconstruida y pronóstico. Es una observación adicional a las cinco del §5.

Fuentes de comprobación: [cuaderno ejecutado de E2](Entrega2_Equipo8_ejecutada.ipynb), partes 1A §§2–8, 1B §§10–14 y 1C §§1–4; [informe de E2](Informe_Entrega2_Equipo8.pdf), §§1 y 2.3; [rúbrica oficial de E2](https://github.com/LuisRojo-Gonzalez/Operations-Management/blob/main/CaseStudy/Rubricas/Entrega_2.pdf), dimensión «Rigor técnico, decisiones e integración».
