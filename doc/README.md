Documentación del Módulo de Informe de Ventas
=============================================

1. Instalación
-------------

Para instalar el módulo de Informe de Ventas en Odoo, sigue estos pasos:

1. Clona el repositorio:
    ```
    git clone https://github.com/frsuleGH/prueba_AITIC.git
    ```
2. Coloca el módulo en la carpeta de custom:
    Copia la carpeta del módulo `ventas_aitic` en el directorio de odoo/sources/repositories/custom/ de Odoo y reinicia el servidor.
3. Actualiza la lista de módulos:
    Inicia Odoo y ve a la interfaz de administración. Actualiza la lista de módulos desde el menú de aplicaciones en modo desarrollador.
4. Instala el módulo:
    Busca "prueba_AITIC" en la lista de aplicaciones y haz clic en "Instalar".
    Activa en ventas descuento

2. Contenido del módulo:
---------------------

### 1. Gestión de Descuentos para clientes con productos.

Ingresa al módulo Descuentos y selecciona nuevo, carga el cliente, producto y el porcentaje de descuento automatizado que va a utilizar.

#### Gestión de Descuentos:

El módulo incluye una vista de árbol que muestra todos los descuentos configurados, mostrando el cliente, el producto y el porcentaje de descuento. Además, ofrece una vista de formulario para crear y editar descuentos, permitiendo al usuario definir los detalles del descuento.

La funcionalidad principal del módulo es la aplicación automática del descuento a las ventas que involucran el producto y el cliente especificos. Esto se logra a través de la integración con el módulo de Ventas, que aplica el descuento correspondiente a las líneas de orden de venta que coinciden con los descuentos configurados.

El módulo también incluye una restricción para evitar la creación de descuentos duplicados para el mismo cliente y producto, asegurando que cada combinación de cliente y producto tenga un descuento único.

El archivo `discount.py` define el modelo `CustomerProductDiscount` que gestiona los descuentos específicos para cada cliente y producto. Este modelo incluye campos para el cliente, el producto y el porcentaje de descuento. Además, implementa una restricción para evitar la creación de descuentos duplicados para el mismo cliente y producto, asegurando la unicidad de cada combinación de cliente y producto.

El archivo `sale_order_line.py` modifica el modelo `sale.order.line` para incluir un campo adicional llamado `sol_discount` que representa el descuento específico para cada línea de orden de venta. Además, define un método `_aplicar_descuento_personalizado` que se activa automáticamente cuando se cambian el producto o el cliente de una línea de orden de venta.

Este método busca un descuento específico para el cliente y el producto seleccionados en la línea de orden de venta. Si se encuentra un descuento, se aplica a la línea de orden de venta y se actualiza el campo `sol_discount`. Esto permite una gestión más precisa de los descuentos para cada cliente y producto en las órdenes de venta.

#### Informes de Ventas Mensuales:

El módulo de Informes de Ventas Mensuales ofrece una visión detallada de las ventas realizadas en un rango específico de fechas. A continuación, se describe la funcionalidad de los archivos clave involucrados en este módulo:

* `informe_ventas.py`: Este archivo define el modelo `informe.ventas` que representa el informe de ventas. El modelo incluye campos para el nombre del informe, la fecha de inicio y fin, y una relación con las órdenes de venta. El método `action_generate_report` busca las órdenes de venta dentro del rango de fechas especificado, las asigna al campo `sale_order_ids` y genera el informe.
* `informe_ventas_report.xml`: Este archivo define el template del informe de ventas. El informe muestra un resumen de las ventas, incluyendo la fecha de inicio y fin, y una tabla que lista los productos vendidos, los clientes y los ingresos totales. El informe se genera para cada orden de venta encontrada dentro del rango de fechas.
* `informe_ventas_views.xml`: Este archivo define las vistas y acciones relacionadas con el informe de ventas. Incluye una vista de formulario para definir el rango de fechas del informe, un botón para generar el informe y una acción para llamar al informe. También define el menú y la acción para acceder al informe de ventas.

#### Modificación del Informe de Orden de Venta:

El archivo `sale_order_custom.py` modifica el modelo `sale.order` para incluir tres campos adicionales:

* `campo_personalizado_1`: Un campo de texto que permite al usuario agregar información adicional relevante para la orden de venta.
* `campo_personalizado_2`: Un campo numérico que puede almacenar valores como cantidades adicionales o datos numéricos relacionados con la orden de venta.
* `campo_personalizado_3`: Un campo de fecha que permite al usuario registrar fechas importantes relacionadas con la orden de venta, como fechas de eventos o plazos.

El archivo `campos.xml` define una vista de formulario para la orden de venta que incluye los tres campos personalizados mencionados anteriormente. Esto permite al usuario visualizar y editar estos campos directamente en la interfaz de usuario de Odoo.

El archivo `ir_actions_report_templates.xml` modifica el informe de orden de venta para incluir los tres campos personalizados. Esto permite que los informes de orden de venta generados incluyan la información adicional proporcionada por el usuario en estos campos, lo que puede ser útil para incluir detalles específicos de la orden de venta en el informe.
