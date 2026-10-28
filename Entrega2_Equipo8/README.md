# Entrega 2 — Equipo 8

Un único notebook calcula los resultados heredados de calidad y pronóstico y resuelve la planificación de las 13 semanas. Los archivos de `Entrega1_Equipo8/` permanecen intactos.

[Abrir en Colab](https://colab.research.google.com/github/Jozen1/EntregasGO_Equipo8/blob/main/Entrega2_Equipo8/Entrega2_Equipo8.ipynb) · [Ver ejecución guardada](Entrega2_Equipo8_ejecutada.ipynb)

## Ejecución

Python 3.11 o superior; validado con Python 3.12. Desde la raíz del repositorio:

```bash
python Entrega2_Equipo8/run.py
```

El ejecutor instala las dependencias fijadas y detiene la ejecución ante cualquier error. En Colab abrir `Entrega2_Equipo8.ipynb` y seleccionar **Entorno de ejecución → Ejecutar todo**. La corrida completa puede tardar varios minutos. No exige subir CSV: usa el repositorio docente y una revisión fija. El modo `completo` ejecuta base, referencias y sensibilidades; `base` omite las comparaciones.

## Modelo y decisiones explícitas

- Producción bruta con rendimiento heredado; litros por caja reales y sobrellenado. Lotes mínimos, preparación, capacidad, horas extra y lead time de jarabe de una semana.
- Inventario y atraso mutuamente excluyentes por SKU y semana.
- Seguridad `z × sigma_h` como meta operativa con déficit explícito y penalización proxy separada. Se prueban seguridad estricta y penalización de seguridad 0,5× y 2×. No se afirma cumplimiento del servicio contractual cuando hay déficit.
- Base condicionada a jarabe preparado antes del horizonte: cantidad calculada por familia, no dato observado. El escenario sin jarabe inicial prueba la dependencia de este supuesto. No hay costo ni volumen inicial informado en el caso.
- L1 sin horas extra en la base por faltar tarifa; sensibilidad con tarifa imputada. Preparaciones de envasado promediadas por familia y mezcla con 1,2 h por familia activa. El secuenciamiento detallado se contrasta en la entrega final.
- Semana 12 exige producción vendible mínima según la cartera oficial (§7.1 del enunciado). Los plazos de despacho por día y hora no se resuelven aquí.
- Reserva terminal dura: seguridad y, para CIT/FUN, una semana al máximo de demanda de las semanas 10–13. Se exige atraso final cero. No se denomina pronóstico de enero a esta política.

## Salidas e interpretación

`Avance2_Equipo8/resultados/` contiene `corridas.csv`, entorno y hashes; cada escenario tiene configuración, estado, cota, brecha, tiempo, modelo LP y log. Solo las soluciones factibles tienen planes y costos. El costo objetivo incluye la penalización proxy de seguridad; `costo_operativo_clp` la excluye. El servicio semanal FIFO se calcula sobre el pronóstico, no sobre despachos reales.

El verificador reconstruye balances, exclusión inventario/atraso, seguridad y sus déficits, lotes, capacidades, lead time, cartera, terminal y costos. El puente guarda `semana12.csv`, `puente_semana12_recursos.csv` y `puente_semana12_campanas.csv`. El notebook genera gráficos y un ZIP de las salidas.

La referencia literal lote por lote se comprueba bajo las mismas restricciones; si es infactible, no se le asigna costo ni ahorro ficticio. La referencia reparada usa campañas predefinidas y optimización lexicográfica: no es una heurística pura. Las sensibilidades muestran costo, inventario, horas extra y servicio; diferencias entre incumbentes con brechas abiertas no prueban superioridad de una política. Los costos unitarios marginales son referencias económicas, no precios sombra del MIP.

Los supuestos faltantes del caso siguen visibles. Los resultados se deben defender bajo esos supuestos. El informe debe declarar la asistencia de IA en programación y revisión, según el enunciado.
