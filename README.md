





# 🚀 Proyecto Integrador: TechStore Online

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.s.hields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

### Informe de Avance y Estado del Proyecto

**Fecha:** 8 de agosto de 2025

**TechStore Online** es una aplicación web de comercio electrónico desarrollada con el framework Django que ha evolucionado de un prototipo a una plataforma robusta. El proyecto cumple con el 100% de la funcionalidad principal operativa del Sprint 3 y permite a los usuarios navegar por un catálogo de productos, gestionar un carrito de compras y realizar pedidos de forma segura.

---

## ✨ Funcionalidades Clave

* **Autenticación de Usuarios**: Sistema robusto de registro y login que permite a los usuarios interactuar de forma segura.
* **Catálogo de Productos**: Vista dinámica y completamente funcional que muestra los productos con sus detalles e imágenes asociadas.
* **Búsqueda Avanzada**: Permite a los usuarios filtrar productos por nombre, descripción o precio.
* **Carrito de Compras Persistente**:
    * Los usuarios pueden agregar, eliminar y actualizar la cantidad de productos.
    * El sistema calcula el total de la compra y los subtotales de forma precisa.
    * La lógica del carrito está basada en sesiones de Django, lo que garantiza la persistencia.
* **Gestión de Pedidos**:
    * Los usuarios autenticados pueden procesar su carrito y convertirlo en un pedido formal.
    * Se han creado los modelos `Pedido` y `DetallePedido` para registrar las órdenes en la base de datos.
    * Se ha verificado que la funcionalidad de guardado es correcta a través del panel de administración.
* **Panel de Administración (Django Admin)**: Un panel de gestión completo para los modelos `Producto`, `Categoría`, `Usuario`, `Pedido` y `DetallePedido`.
* **Manejo de Archivos**: Las rutas `STATIC_URL` y `MEDIA_URL` han sido definidas y validadas para la correcta carga de estilos e imágenes.

---

## 🛠️ Tecnología y Arquitectura

* **Backend**: Desarrollado con el framework **Django**.
* **Base de Datos**: Configurada con **SQLite** como motor predeterminado (`db.sqlite3`).
* **Frontend**: Utiliza **Bootstrap** para un diseño responsivo.
* **Control de Versiones**: El proyecto se gestiona en un repositorio de **GitHub**.

---

## 💻 Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener Python y un entorno virtual configurado.

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/Luisfernandovallejomontoya/django_techstore.git](https://github.com/Luisfernandovallejomontoya/django_techstore.git)
cd django_techstore
