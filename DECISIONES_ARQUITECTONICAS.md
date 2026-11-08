# Evaluación Crítica - Decisiones Arquitectónicas

## 1. ¿Qué nueva dependencia hicieron explícita?
Hicimos explícita la dependencia hacia el puerto de salida de inventario (`PuertoInventario`). De esta forma, el caso de uso define el contrato abstracto que necesita para verificar y reservar stock sin acoplarse a proveedores concretos.

## 2. ¿Qué dependencia invirtieron o aislaron?
Se aisló la API de terceros `StockCloudAPI` utilizando un adaptador (`StockCloudAdapter`). El servicio de aplicación ya no llama directamente a la API externa ni conoce sus métodos específicos (`query_stock`, `reserve_units`).

## 3. ¿Qué detalle externo quedó fuera del núcleo?
Quedaron fuera del núcleo los formatos de los diccionarios de la API REST simulada, la lógica de lectura/iteración de archivos en lote (*batch*) y la estructura de respuestas y códigos propios de `StockCloudAPI`.

## 4. ¿Qué cambio futuro quedó localizado?
Si se decide cambiar de proveedor de inventario (por ejemplo, reemplazar StockCloud por otro servicio) o agregar nuevos canales de entrada (como GraphQL o una interfaz CLI), el cambio queda estrictamente localizado en los adaptadores correspondientes, sin tocar el núcleo de la aplicación.

## 5. ¿Qué complejidad adicional introdujo su solución?
Se introdujo una capa adicional de indirección mediante adaptadores y clases de traducción entre las estructuras externas y lo que requiere el dominio.

## 6. ¿Qué abstracción decidieron no crear y por qué?
Decidimos no crear frameworks web pesados (como Flask o FastAPI), ni buses de eventos avanzados, ni patrones complejos de CQRS. El tamaño y alcance del problema se resuelve limpiamente con adaptadores de entrada y salida simples en Python puro.
