# Validación de la Entrega 2

La revisión se hizo por etapas en Python 3.12 con los paquetes fijados. Se recalculó el traspaso de Entrega 1 desde los CSV oficiales y se comprobaron sus 117 filas con la huella de la corrida anterior. Los límites normales fueron 180 s para la base, 90 s para sensibilidades y 30 s por etapa de reparación de la referencia. La validación se realizó en el entorno local.

La corrida base archivada y las sensibilidades corresponden al registro de HiGHS. El estado por límite de tiempo admite una solución factible con una brecha abierta. El costo reportado en el PDF reproduce esa corrida. El informe señala el estado, la cota y los costos de la base y remite a las tablas para las comparaciones.

La auditoría independiente revisó 27 planes, incluidas las etapas auxiliares de la referencia. Abarca los balances, los límites de capacidad, la cartera de la semana 12, el uso del jarabe, la reserva terminal y la reconstrucción de costos. Las pruebas de alteración confirmaron que el verificador rechaza un cambio en la cantidad de la semana 12, en el jarabe que llega desde la semana 11 o en el costo de producción.

La corrida con seguridad estricta y jarabe inicial de base resultó infactible. Se verificaron dos alternativas que satisfacen la meta de seguridad en cada SKU y semana: 15 % de jarabe inicial adicional por familia y uso de horas extra de L1 a tarifa imputada. Las configuraciones y planes se guardan en `resultados_verificados`.

La regla lote por lote supera la capacidad de L1 en seis semanas. El diagnóstico está en `resultados_verificados/lfl_literal`. El puente de semana 12 registra el jarabe recibido y consumido, los lotes y las horas de preparación de cada recurso.
