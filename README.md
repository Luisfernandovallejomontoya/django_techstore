Proyecto Integrador - TechStore Online
Informe de Avance del Proyecto Integrador - Módulo 3

Fecha: 6 de agosto de 2025

Para: Profesor Hanz Saenz, Catedrático de enyoi.co
De: Luis Fernando Vallejo Montoya
Asunto: Estado del proyecto TechStoreOneline

Estimado Profesor Hanz Saenz,

Por medio de este informe, detallo el estado actual del proyecto TechStoreOneline, enfatizando las funcionalidades que ya han sido implementadas, los avances significativos en los módulos pendientes y la tecnología utilizada, logrando un 100% de la funcionalidad principal operativa del Sprint 3. El proyecto se ha transformado de un prototipo web a una plataforma robusta con un backend real y una lógica de negocio centralizada.

1. Estructura y Funcionalidades Implementadas
La estructura principal del proyecto ha sido validada y se encuentra en un estado funcional, cumpliendo con los requisitos del Sprint 3.

Autenticación de Usuarios: Se ha implementado un sistema de autenticación de usuarios que permite el registro y el inicio de sesión. Esta funcionalidad es clave para que los clientes puedan interactuar con el sistema de forma autenticada. Se ha superado el desafío inicial de compatibilidad de librerías para lograr su integración.

Módulo de Catálogo de Productos: El catálogo de productos está completamente operativo. La vista dinámica renderiza la lista de productos disponibles, mostrando su información y las imágenes asociadas de manera correcta.

Carrito de Compras: La funcionalidad del carrito de compras ha sido implementada y validada por completo, superando los desafíos iniciales. El sistema ahora permite:

Agregar, eliminar y actualizar la cantidad de productos.

Calcular automáticamente el total de la compra, incluyendo los subtotales de cada artículo. Esta funcionalidad ahora muestra el total de forma correcta, resolviendo el problema de inconsistencia previamente detectado.

Panel de Administración (Django Admin): El panel de administración de Django está conectado de forma exitosa y directa con la base de datos. Esto permite la gestión completa (CRUD) de los modelos de la aplicación, como Producto y Categoría.

Manejo de Archivos Estáticos y Media: Las rutas STATIC_URL y MEDIA_URL han sido definidas y validadas, garantizando que los estilos, scripts e imágenes de los productos se carguen y se muestren correctamente.

2. Tecnología y Arquitectura Implementada
Backend: Se ha construido un backend robusto y escalable utilizando el framework Django. La lógica de negocio está centralizada en el servidor, separando la lógica de la presentación.

Base de Datos: El proyecto está configurado para utilizar SQLite, la base de datos por defecto de Django, con una conexión completamente funcional. La base de datos del proyecto se encuentra en la ruta db.sqlite3 dentro del directorio principal del proyecto.

Control de Versiones: El proyecto está alojado en un repositorio de GitHub, lo que facilita la colaboración y el seguimiento de los avances.

3. Funcionalidades Pendientes y Próximos Pasos
El proyecto ha alcanzado el 100% de las funcionalidades principales del Sprint 3. Los próximos pasos se centrarán en las funcionalidades adicionales y la optimización del proyecto:

Gestión de Pedidos: Aún está pendiente la implementación de la creación de pedidos, la consulta del historial de pedidos por usuario, y la gestión de pedidos por parte del administrador para cambiar su estado (pendiente, en proceso, enviado, entregado).

Integración de Métodos de Pago: Se debe implementar el soporte para múltiples métodos de pago (tarjeta de crédito, transferencia bancaria y pago contraentrega) y el sistema de confirmación de pagos.

Refactorización y optimización: Mejorar la estructura y eficiencia del código implementado, así como documentar la API.

Agradezco de antemano su tiempo y valiosa consideración.

Atentamente,

Luis Fernando Vallejo Montoya.
cc.75096889
ce:luisfernandovallejomontoya@gmail.com