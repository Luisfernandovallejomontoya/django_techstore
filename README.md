
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



📝 Propuesta de Actualización para el README.md
🚀 Proyecto Integrador: TechStore Online + Agromaker AI

Informe de Actualización y Estado del Proyecto
Fecha: 13 de febrero de 2026

TechStore Online ha evolucionado de ser un e-commerce tradicional a una plataforma integral que fusiona el comercio tecnológico con la Sostenibilidad Digital y la Inteligencia Artificial. Actualmente, el proyecto integra el módulo Agromaker AI, diseñado para el monitoreo climático y la gestión de riesgos agrícolas en la región de Filadelfia, Caldas.



✨ Funcionalidades Clave (Actualizadas)🌱 Módulo Agromaker AI (NUEVO):Análisis Climático de Filadelfia: Sistema de IA que procesa datos de pluviosidad en tiempo real.Semáforo de Riesgo Inteligente: Lógica predictiva basada en umbrales (Verde: Normal | Amarillo: Alerta $\ge$ 80mm | Rojo: Peligro $\ge$ 120mm).Dashboard de Sostenibilidad: Visualización de registros climáticos históricos y actuales (Registro actual: 81.6 mm - Estado Amarillo).



🛒 E-Commerce Robusto:

Gestión de carrito de compras persistente basada en sesiones de Django.

Sistema de pedidos con modelos Pedido y DetallePedido vinculados al perfil de usuario.

🔐 Seguridad y Autenticación: Registro y Login validados con control de acceso a funciones administrativas.



🛠️ Tecnología y Arquitectura
Backend: Django 4.x / 5.x.

Inteligencia Artificial: Lógica de procesamiento de datos en el módulo agromaker_ai.

Base de Datos: SQLite (db.sqlite3) con registros climáticos actualizados al 2026.

Frontend: Bootstrap con visualización dinámica de alertas de color neón.



💻 Instalación y Uso
Clonar: git clone https://github.com/Luisfernandovallejomontoya/django_techstore.git

Activar Entorno: .\venv_entorno\Scripts\activate

Ejecutar: python manage.py runserver


### ✅ Fase de Reportes Técnicos (Completada 23-Feb-2026)
* **Generación de Reportes Excel:** Implementación de exportación automática con la librería `openpyxl`.
* **Consistencia de Datos:** Validación de datos satelitales (82.3 mm para Filadelfia) exportados con formato profesional.
* **Semáforo de Riesgo:** Integración total entre la IA del Dashboard y los informes descargables.