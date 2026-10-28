# Formulación y lectura del modelo

## Unidades y variables

Para SKU i, familia f, línea l y semana t=1,…,13:

- x: producción bruta, cajas; y: binaria de preparación por SKU.
- I: inventario vendible, cajas; B: demanda atrasada, cajas.
- U: déficit frente a la meta de seguridad, cajas; z: binaria que distingue inventario de atraso.
- Q: jarabe mezclado, litros; J: jarabe disponible al cierre, litros; W: activación de mezcla por familia.
- A: familia activa en una línea; Z: ambos formatos de L2 activos para esa familia.
- O: horas extra por recurso y semana.

El rendimiento es eta=1−rho, donde rho es la **tasa de merma** heredada; no se confunde rho con rendimiento. Los litros por caja bruta son a=litros nominales por caja + sobrellenado mL/botella × botellas/caja ÷ 1.000. El sobrellenado y la merma se aplican una sola vez.

## Balance, preparación y capacidad

`I_it − B_it = I_i,t−1 − B_i,t−1 + eta_i x_it − d_it`.

I_i0 viene del CSV y B_i0=0. Se impone que los envíos inferidos, d_it+B_i,t−1−B_it, sean no negativos. El costo de atraso es por caja **y semana**: sumar B no equivale a contar pedidos distintos.

`lote_i y_it ≤ x_it ≤ M_it y_it`.

M se obtiene de la tasa por SKU multiplicada por las horas regulares más extra permitidas menos una preparación de su familia. Es una cota superior individual; las restricciones compartidas siguen siendo necesarias. El inventario máximo se acota por I_i0 más toda la producción vendible acumulable hasta t; el atraso máximo, por toda la demanda llegada hasta t. Estas cotas enlazan z para impedir I>0 y B>0 simultáneamente.

La suma de horas de producción x/tasa y preparación no supera horas regulares más O. O está acotada por el CSV. Las mantenciones ya están descontadas: no se restan dos veces. A es el OR de las preparaciones de SKU de la familia/línea; Z es el AND de los dos formatos de L2. Una familia activa consume el CIP promedio entrante obtenido de la matriz oficial; ambos formatos de L2 añaden 0,6 h y 38.000 CLP. Se prueba también el máximo entrante en una sensibilidad. Es una aproximación semanal, no una secuencia física detallada.

## Flujo de jarabe

`J_ft = J_f,t−1 + Q_f,t−1 − suma_i_en_f(a_i x_it)`.

Q_f0=0: Q de la semana t alimenta envasado a partir de t+1. La mezcla consume Q/tasa más 1,2 h por familia activa. Q se enlaza a W mediante una cota derivada de capacidad. Cobrar CIP incluso a la primera familia es una aproximación conservadora explícita.

J_f0 no está en los datos. En la base se fija fuera del optimizador sumando por familia el jarabe para cubrir, al arranque, `max(0,(d_i1+SS_i1−I_i0)/eta_i)`, respetando lote mínimo cuando se requiere producción. Se calcula siempre con servicio y merma base para comparar escenarios, y se exporta. Es un escenario de preparación previa, no una existencia medida ni producción gratuita certificada. La variante J_f0=0 revela la dependencia del arranque. No hay límite de almacenamiento informado; se prueban J=0 y costo de almacenamiento imputado. Se restaura al final al menos J_f13+Q_f13 ≥ J_f0, salvo la sensibilidad sin protección terminal.

## Seguridad e incertidumbre

Si el error de pronóstico al horizonte h es aproximadamente normal con desviación sigma_i,h, la condición marginal `P(error ≤ SS) ≥ NS_i` lleva a `SS=Phi^−1(NS_i) sigma_i,h`. Sigma se obtiene fuera de muestra en desarrollo de Entrega 1. No se multiplica otra vez por raíz del horizonte: no es una desviación semanal independiente que se esté acumulando. El lead time físico de jarabe se representa por el desplazamiento de Q. La fórmula de seguridad es una aproximación marginal, no garantía de servicio conjunto en 13 semanas.

La versión operativa permite `I_it+U_it ≥ SS_it`, con `0≤U_it≤SS_it`. Se penaliza U con el costo por caja-semana de atraso como proxy separado; no es un costo contractual observado. Se prueban 0,5× y 2× y la variante estricta U=0. Un plan con U>0 **no cumple toda la meta de seguridad**, aunque sea factible para la formulación elástica. Esto se reporta explícitamente en el cuadro de mando.

## Frontera y semana focal

B_i13=0. La reserva terminal es SS_i13 para NEC; para CIT/FUN se suma una semana al máximo de d_i10,…,d_i13. Es protección al cerrar diciembre usando información disponible, no un pronóstico de enero. Las variantes sin reserva adicional y con media semana cuantifican el efecto.

`eta_i x_i12 ≥ cartera_i` cumple la producción mínima pedida en §7.1 del enunciado. La cartera se agrega por SKU. No se suma de nuevo a la demanda porque no hay evidencia de que sea demanda adicional al pronóstico. El puente conserva cartera, producción, línea, activaciones y horas supuestas para secuenciar la semana 12 en la entrega final. El plazo por día/hora no está garantizado por un plan semanal.

## Función objetivo y lectura económica

Se minimizan producción bruta a costo variable; inventario de producto terminado; atraso; CIP de envasado y mezcla; cambios de formato; horas extra; almacenamiento de jarabe si se imputa; y penalización proxy U. El costo operativo exportado excluye esta última penalización. No se añaden salarios regulares ni ingreso por ventas porque no son decisiones marginales de este modelo.

La tarifa extra L1 falta: se deshabilita en la base. La sensibilidad que la habilita usa la tarifa L2 como imputación, identificada como supuesto. No se presenta como dato oficial.

Se comparan 95 CLP por caja por adelantar una semana, 1.400 por atrasar una semana y los costos de horas extra por caja vendible, convirtiendo litros y rendimiento. Son referencias unitarias: preparaciones, lotes y capacidad pueden cambiar la decisión conjunta. No son precios sombra del MIP.

HiGHS informa costo de la solución, cota inferior, brecha y tiempo. Una solución factible bajo límite de tiempo no es un óptimo demostrado. Las sensibilidades vuelven a resolver; para parámetros que cambian costos no se compara su objetivo como si fuera una misma tarifa. Las diferencias pequeñas entre incumbentes con brechas abiertas no demuestran ahorro causal. La referencia reparada tiene una política de campañas fijada antes del MIP; su subproblema también usa optimización y así se declara.
