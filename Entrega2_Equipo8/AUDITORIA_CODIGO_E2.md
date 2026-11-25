# Auditoría del código de planificación de la Entrega 2

Se revisó [la versión 4b05c62](https://github.com/Jozen1/EntregasGO_Equipo8/tree/4b05c6218fbcbc46426ecc75556459c3eb5fedb4/Entrega2_Equipo8), especialmente las funciones `read_data`, `build_model`, `solve`, `kpis`, `verificar` y `main` del [cuaderno](Entrega2_Equipo8.ipynb). El contraste académico corresponde al [enunciado, §§7.1–7.3](https://github.com/LuisRojo-Gonzalez/Operations-Management/blob/main/CaseStudy/Enunciado.pdf). Las observaciones de esta auditoría se suman a la [revisión del feedback de E1](REVISION_FEEDBACK_E1.md).

## Comparaciones económicas que conviene corregir

Las tres corridas terminaron por tiempo. El ejecutor entrega a algunas sensibilidades el plan base como solución inicial, pero no cruza sistemáticamente las soluciones compatibles entre escenarios. En estos tres casos se construyó una alternativa factible de menor costo **con los mismos parámetros de cada escenario**. Son cotas superiores alcanzables. La diferencia de la última columna se mide respecto de la solución publicada de esa misma fila.

| Escenario | Objetivo publicado (CLP) | Objetivo factible comprobado (CLP) | Mejora (CLP) |
|---|---:|---:|---:|
| Servicio objetivo −2 puntos porcentuales | 951.296.301 | 950.873.309 | 422.991 |
| Sin restitución terminal de jarabe | 955.156.146 | 950.888.201 | 4.267.945 |
| Horas extra de L1 a tarifa imputada | 951.065.801 | 947.678.555 | 3.387.246 |

Cada monto y cada diferencia se redondearon independientemente al peso. Los costos son objetivos del modelo, incluida la penalización referencial por déficit de seguridad.

1. **Servicio −2 puntos.** Se mantuvo la producción, el inventario y las horas de la base. Se recalcularon la protección semanal y la reserva terminal con el nuevo nivel, y el déficit como el máximo entre cero y protección menos inventario. El jarabe inicial queda fijo por construcción. El déficit del candidato suma 783,97 caja-semanas. El plan cuesta unos $192.492 menos que la base bajo la tarifa del escenario. La tabla 3 del informe muestra un mayor objetivo para el escenario relajado porque compara dos soluciones obtenidas al agotarse el tiempo. No permite inferir el efecto económico de relajar el servicio.
2. **Sin restitución de jarabe.** El modelo fija en cero la mezcla de la semana 13 en este escenario. Por el desfase de una semana, esa mezcla alimentaría la semana 14. Se tomó el plan base y se anularon los 41.518,67 L que iba a mezclar en la semana 13, las dos activaciones asociadas y sus 2,4 h de preparación. La mezcla no usaba horas extra esa semana. Desaparecen $177.600 de CIP respecto de la base, conservando producción, seguridad, inventario de producto terminado y cartera.
3. **Horas extra de L1.** El [plan publicado con horas extra de L1 y seguridad estricta](resultados_verificados/seguridad_extra_L1/plan_sku.csv) ya satisface la versión con seguridad flexible. Se comprobó ese mismo plan bajo la configuración flexible, incluida la tarifa imputada. Utiliza 8,65 h extra en L1 y su déficit de seguridad es cero. La comparación publicada para `OT_L1_imputada` subestima lo que se puede conseguir con esas horas.

**Corrección propuesta.** Usar estos planes como candidatos iniciales específicos de cada escenario, reajustar sus variables auxiliares e incorporar una prueba de consistencia antes de publicar la tabla. Si al límite de tiempo el solver entrega un candidato más caro que uno ya validado, conservar el mejor factible y su procedencia. Reportar por separado el costo alcanzable, la cota inferior y la brecha calculada con ambos. Recalcular también inventario, horas y déficit de la fila elegida.

## Qué comprueba el verificador y qué queda fuera

Se volvió a ejecutar el verificador de la entrega sobre copias temporales del [plan base](resultados_verificados/base). Pasaron los 2.949 controles. El desbalance máximo de producto terminado fue inferior a 0,000001 cajas y el de jarabe inferior a 0,000001 L. El objetivo reconstruido fue $951.065.801. A partir del plan detallado se calcularon 14.620,32 cajas de inventario medio, rotación de 11,93 veces en 13 semanas y servicio semanal FIFO del 100 % sobre la demanda pronosticada.

Los tres candidatos anteriores pasaron los controles de factibilidad y reconstrucción de costos de su escenario. Para los dos candidatos construidos aritméticamente se omitió la comparación con un objetivo emitido por el solver, pues no hubo una nueva optimización. La verificación del candidato reutilizado de L1 también concuerda con su objetivo de solver archivado.

**Prueba del resumen.** En una copia temporal se sustituyó en `registro.json` el servicio FIFO por 50 % y el inventario medio por cero, conservando intacto el plan detallado. Pasaron los mismos 2.949 controles. El verificador reconstruye restricciones y costo, pero no coteja esos indicadores del resumen. Conviene derivarlos de los CSV y comprobarlos antes de exportar `corridas.csv` y las tablas del informe.

**Archivo de resultados.** En [corridas.csv](resultados_verificados/corridas.csv) aparecen 24 escenarios principales, de los cuales 21 son factibles. En esa versión de GitHub hay planes detallados de tres: base, seguridad estricta con jarabe adicional y seguridad estricta con horas extra de L1. El detalle de los otros 18 planes factibles no se puede volver a verificar desde ese archivo. Archivar al menos los planes, las configuraciones y los desgloses de costo utilizados en la tabla 3 y en la comparación con la política de referencia. Reoptimizar puede producir un plan diferente por el límite de tiempo.

## Aislar el efecto del jarabe inicial

La sensibilidad `seguridad_jarabe_mas15` compara seguridad estricta con 15 % más de jarabe inicial; frente a `seguridad_estricta`, el cambio de stock inicial también eleva la obligación terminal. La función `read_data` multiplica el inventario inicial por 1,15 y `build_model` exige restituir al menos ese monto por familia, contando stock y mezcla en tránsito. Los litros iniciales y el mínimo terminal pasan ambos de 60.466,23 a 69.536,17. El resultado publicado responde a la pregunta «¿qué ocurre si arranco con más y debo reponer ese nivel al cierre?». Para medir solo el efecto del arranque, definir por separado stock inicial y meta terminal, conservar la meta original y comparar ambos escenarios con seguridad estricta.

Alcance: inspección de código, contraste con el enunciado, comparación con resultados archivados y comprobaciones aritméticas en copias temporales. Las huellas de los tres scripts embebidos coinciden con el manifiesto de controles. El modelo no fue reoptimizado ni se modificaron el código o los resultados originales.
