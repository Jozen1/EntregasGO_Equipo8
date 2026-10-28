# Validación de la Entrega 2

Ejecución local completa con versiones fijadas y límites normales: base 180 s, sensibilidades 90 s y referencia 30 s por etapa. Se ejecutaron las celdas de cálculo y el optimizador sin modo de prueba rápida. La sesión local se interrumpió antes de terminar la última sensibilidad; esa sensibilidad se ejecutó después con su configuración normal y se reconstruyeron y verificaron las tablas y celdas finales. No se afirma una corrida ininterrumpida completa. La instalación inicial se omitió en la prueba local porque se comprobaron previamente las versiones exactas instaladas. No se afirma prueba de la interfaz Colab.

Datos docentes a revisión fija; el traspaso se recalculó desde calidad y pronóstico en esta ejecución. No se modificó Entrega 1. Los tres gráficos de nueve series mantienen eje vertical compartido dentro de cada figura.

## Resultado de la ejecución

- Estado base: kTimeLimit; costo objetivo: 949,483,282.31 CLP; cota: 945,510,297.30 CLP; brecha: 0.4184%.
- Costo operativo sin penalización proxy de seguridad: 948,355,192.45 CLP.
- Servicio semanal FIFO estimado sobre pronóstico: 100.0000%; no equivale a servicio contractual observado.
- Déficit de seguridad: 805.7785 caja-semanas. Inventario y atraso simultáneos: cero pares SKU-semana.
- 24 planes con verificación aritmética independiente. Base: 2942 controles. Se comprobó además que el verificador rechaza alteraciones en producción, inventario y déficit de seguridad.
- 117 filas SKU-semana y atraso final cero. Cantidades y preparaciones de semana 12 congeladas en `base/`.

El escenario base supone jarabe preparado antes del horizonte. Es un supuesto inicial exportado, no un inventario observado. La comparación incluye seguridad estricta y arranque sin jarabe. Los escenarios infactibles se conservan como tales. El estado y brecha de cada escenario figuran en `comparacion.csv`; no se atribuyen a sensibilidades pequeñas diferencias entre soluciones no óptimas.

## Criterio económico

Se muestran costos por caja vendible para adelantar una semana (95 CLP), atrasar una semana (1.400 CLP), y usar horas extra de mezcla/envasado. Adelantar puede ser más barato por unidad que horas extra, siempre que exista capacidad y considerando preparaciones. El MIP evalúa conjuntamente esas restricciones. Las comparaciones unitarias son referencias, no precios sombra ni prueba de optimalidad.

## Alcance de la entrega

Código, configuración, verificación, sensibilidad y resultados terminados bajo los supuestos documentados. El informe y la exposición deben usar estas salidas y justificar el jarabe inicial, la relajación de seguridad, los promedios CIP y la política terminal; no se sustituyen por una garantía de datos que el caso no entrega. Debe declararse la asistencia de IA según el enunciado.
