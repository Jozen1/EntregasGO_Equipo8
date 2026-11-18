# Entrega 2 — Equipo 8

Un único notebook calcula los resultados heredados de calidad y pronóstico y resuelve la planificación de las 13 semanas. Los archivos de `Entrega1_Equipo8/` permanecen intactos.

[Abrir en Colab](https://colab.research.google.com/github/Jozen1/EntregasGO_Equipo8/blob/main/Entrega2_Equipo8/Entrega2_Equipo8.ipynb) · [Ver ejecución guardada](Entrega2_Equipo8_ejecutada.ipynb)

## Ejecución

Python 3.11 o superior; validado con Python 3.12. Desde la raíz del repositorio:

```bash
python Entrega2_Equipo8/run.py
```

El ejecutor instala las dependencias fijadas y verifica los datos de `datos/crudos/` contra la revisión docente. En Colab, abrir `Entrega2_Equipo8.ipynb` y seleccionar **Entorno de ejecución → Ejecutar todo**. El cuaderno obtiene los datos del repositorio docente cuando se abre fuera del repositorio del equipo. Ambas rutas comprueban las mismas huellas de los archivos. La corrida completa puede tardar varios minutos. El modo `completo` ejecuta base, referencias y sensibilidades. El modo `base` calcula el plan principal.

## Modelo y decisiones explícitas

- Producción bruta con rendimiento heredado; litros por caja reales y sobrellenado. Lotes mínimos, preparación, capacidad, horas extra y lead time de jarabe de una semana.
- Inventario y atraso mutuamente excluyentes por SKU y semana.
- Seguridad `z × sigma_h` como meta operativa con déficit explícito y penalización proxy separada. Se prueba seguridad estricta con los datos base, con 15 % más de jarabe inicial y con horas extra imputadas en L1. También se ensayan penalizaciones de seguridad de 0,5× y 2×.
- Base condicionada a jarabe preparado antes del horizonte: cantidad calculada por familia, no dato observado. El escenario sin jarabe inicial prueba la dependencia de este supuesto. No hay costo ni volumen inicial informado en el caso.
- L1 sin horas extra en la base por faltar tarifa; sensibilidad con tarifa imputada. Preparaciones de envasado promediadas por familia y mezcla con 1,2 h por familia activa. El secuenciamiento detallado se contrasta en la entrega final.
- Semana 12 exige producción vendible mínima según la cartera oficial (§7.1 del enunciado). Los plazos de despacho por día y hora no se resuelven aquí.
- Reserva terminal dura: seguridad y, para CIT/FUN, una semana al máximo de demanda de las semanas 10–13. Se exige atraso final cero. Las sensibilidades retiran por separado la reserva de producto terminado y la restitución de jarabe.

## Salidas e interpretación

`Avance2_Equipo8/resultados/` contiene `corridas.csv`, entorno y hashes; cada escenario tiene configuración, estado, cota, brecha, tiempo, modelo LP y log. Solo las soluciones factibles tienen planes y costos. El costo objetivo incluye la penalización proxy de seguridad; `costo_operativo_clp` la excluye. El servicio semanal FIFO se calcula sobre el pronóstico, no sobre despachos reales.

El verificador reconstruye balances, exclusión inventario/atraso, seguridad y sus déficits, lotes, capacidades, lead time, cartera, terminal y costos. El puente guarda cantidades y horas en `semana12.csv` y `puente_semana12_recursos.csv`. En `puente_semana12_campanas.csv` separa el jarabe disponible para envasar en la semana 12 del jarabe mezclado en esa semana, que se puede usar desde la semana 13. El notebook genera gráficos y un ZIP de las salidas.

La referencia lote por lote fija la producción que propone la regla y utiliza las restricciones y costos del plan base para comprobar si puede abastecerse con jarabe y horas disponibles. Se exporta el diagnóstico semanal de carga de L1. La referencia reparada combina campañas predefinidas con dos etapas de optimización por rotación.

Las sensibilidades registran costo, inventario, horas extra, atraso y servicio. Cuando el plan base sigue siendo factible, se ofrece como punto de partida al solver de ese escenario. Se guardan el costo con la tarifa de atraso de base y, para los cambios de capacidad de mezcla, el intervalo de diferencia de costos que permiten las cotas de ambas corridas. Los costos marginales por caja usan la tarifa de mezcla de la semana 11 y de envasado de la semana 12.

Los supuestos faltantes del caso siguen visibles. Los resultados se deben defender bajo esos supuestos. El informe debe declarar la asistencia de IA en programación y revisión, según el enunciado.
