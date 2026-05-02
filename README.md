# 🚀 Agromaker AI + TechStore Online
### Sostenibilidad Digital e Inteligencia Artificial para el Agro
**Ubicación:** Caldas, Colombia | **Fecha:** 2 de Mayo, 2026
**Soberanía Tecnológica:** Agromaker Colombia (AI) S.A.S.
**Autor:** Ing. Luis Fernando Vallejo Montoya

---

## 🛡️ Estatus del Proyecto: RELEASE v1.3 — OPERATIVO

Plataforma que integra **e-commerce** con **monitoreo climático y de suelos** en tiempo real para los 27 municipios y 16 pisos térmicos de Caldas.

---

## 🔄 Bitácora de Hitos

| Fecha | Hito | Descripción | Estado |
|-------|------|-------------|--------|
| Ago 2025 | Sprint 3 | Catálogo, Carrito, Pedidos (100%) | ✅ |
| Feb 2026 | Agromaker AI | Semáforo de riesgo, análisis satelital | ✅ |
| Feb 2026 | Reportes Técnicos | Exportación Excel (openpyxl) | ✅ |
| Mar 2026 | Suelos & IoT | Monitor pH, PDFs, registro en campo | ✅ |
| Abr 2026 | Caldas 27/16 | Expansión a 27 municipios, 16 pisos térmicos | ✅ |
| **May 2026** | **Refactorización Total** | **Namespaces, AUTH_USER_MODEL, rutas, persistencia GET/POST** | ✅ |

---

## 🛠️ Correcciones Aplicadas (Mayo 2026)

### 🔌 Namespaces (Resuelto: `NoReverseMatch`)
- ✅ `agromaker_ai`: `app_name = 'agromaker_ai'` — URLs: `agromaker_ai:semaforo_ia`, `agromaker_ai:estado_campo`
- ✅ `agromaker_soil`: `app_name = 'agromaker_soil'` — URLs: `agromaker_soil:reporte_campesino`, `agromaker_soil:dashboard_suelos`
- ✅ `productos`: `app_name = 'productos'` — URLs: `productos:catalogo`, `productos:ver_carrito`, `productos:agregar_producto`
- ✅ `usuarios`: `app_name = 'usuarios'` — URLs: `usuarios:login`, `usuarios:logout`, `usuarios:registro`

### 🔐 Auth & User Model
- ✅ `AUTH_USER_MODEL = 'usuarios.CustomUser'`
- ✅ `LOGIN_URL = '/usuarios/login/'` configurado
- ✅ `pedidos/models.py` y `publicidad_ia/models.py` usan `settings.AUTH_USER_MODEL`

### 📡 Persistencia de Parámetros
- ✅ `guardar_semaforo` usa `reverse()` + `urlencode()` para mantener `?municipio=`
- ✅ Formulario POST en `dashboard_clima.html` incluye `?municipio={{ municipio }}`

### 🗺️ Rutas Verificadas
| Módulo | URL | Namespace |
|--------|-----|-----------|
| Hub | `/` | — |
| Admin | `/admin/` | — |
| Catálogo | `/productos/catalogo/` | `productos:catalogo` |
| Carrito | `/productos/ver_carrito/` | `productos:ver_carrito` |
| Login | `/usuarios/login/` | `usuarios:login` |
| Logout | `/usuarios/logout/` | `usuarios:logout` |
| Registro | `/usuarios/registro/` | `usuarios:registro` |
| Semáforo IA | `/agromaker/semaforo/` | `agromaker_ai:semaforo_ia` |
| Dashboard Climático | `/agromaker/dashboard/` | `agromaker_ai:estado_campo` |
| Mapa Satelital | `/agromaker/mapa-satelital/` | `agromaker_ai:mapa_completo` |
| Guardar Sensor | `/agromaker/guardar-semaforo/` | `agromaker_ai:guardar_semaforo` |
| Monitor Suelos | `/suelos/` | `agromaker_soil:reporte_campesino` |
| Dashboard Suelos | `/suelos/dashboard/` | `agromaker_soil:dashboard_suelos` |
| Registro Suelos | `/suelos/registrar/` | `agromaker_soil:registrar_dato` |
| PDF Suelos | `/suelos/exportar-pdf/` | `agromaker_soil:exportar_pdf` |
| Exportar Excel | `/agromaker/exportar/` | `agromaker_ai:exportar_excel` |

---

## ✨ Funcionalidades

### 🌱 Agromaker AI — Monitoreo Climático
- **Semáforo Predictivo:** 🟢 Normal (<80mm) → 🟡 Alerta (≥80mm) → 🔴 Peligro (≥120mm)
- **Dashboard Técnico:** Chart.js, histórico 7 días, recomendaciones IA
- **Mapa Satelital:** Leaflet con geolocalización de lotes
- **Exportación Excel:** Auditorías con openpyxl
- **Registro Manual:** Captura IoT desde tablets → `PrediccionClimatica`

### 🧪 Agromaker Soil — Monitor de Suelos
- **Registro pH + Humedad:** Desde tablets/sensores vía POST
- **Semáforo de Suelos:** 🔴 <5.0 ácido · 🟡 5.0–6.0 vigilancia · 🟢 6.0–7.2 óptimo · 🟠 >80% saturación
- **Certificados PDF:** Generación automática con xhtml2pdf
- **Coherencia de Datos:** `helpers.py` resuelve campos legacy vs nuevos

### 🛒 TechStore — E-Commerce
- Catálogo con búsqueda y filtros
- Carrito persistente por sesión (`Carrito` class)
- Ciclo completo de pedidos (`Pedido` + `DetallePedido`)

---

## ⚖️ Blindaje Jurídico
- **Fondo 305 CEO:** Recursos no negociables
- **Convenio Comodato:** Sensores/tablets — Gobierno de Colombia
- **Propiedad Intelectual:** Agromaker Colombia (AI) S.A.S.
- **Instituciones:** YSA / KOSME

---

## 🛠️ Arquitectura

| Capa | Tecnología |
|------|------------|
| Core | Django 5.x, Python 3.13 |
| Apps | `productos` · `usuarios` · `pedidos` · `agromaker_ai` · `agromaker_soil` · `publicidad_ia` |
| Data | Pandas, Numpy, SQLite → PostgreSQL |
| Front | Bootstrap 5, Chart.js, Leaflet, FontAwesome |
| Reports | openpyxl, xhtml2pdf |
| Deploy | WhiteNoise, Dockerfile |

---

## 💻 Instalación

```bash
# 1. Clonar
git clone https://github.com/Luisfernandovallejomontoya/django_techstore.git
cd django_techstore

# 2. Entorno virtual
.\venv_entorno\Scripts\activate

# 3. Dependencias
pip install django pandas numpy pillow crispy-bootstrap4 whitenoise xhtml2pdf openpyxl

# 4. Migrar y ejecutar
python manage.py migrate
python manage.py runserver
```

**Accesos rápidos:**
- Hub: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Suelos: `http://127.0.0.1:8000/suelos/`
- Dashboard Climático: `http://127.0.0.1:8000/agromaker/dashboard/`

---

## 📋 Flujo de Datos
```
Sensor/Tablet → POST /suelos/registrar/ o /agromaker/guardar-semaforo/
    → IA evalúa umbrales (biology.py, geotechnics.py, semaforo.py)
    → Semáforo asigna estado (VERDE/AMARILLO/ROJO)
    → Dashboard renderiza Chart.js + alertas
    → PDF/Excel exportables para auditoría
```

---

© 2026 Agromaker Colombia AI — Filadelfia, Caldas
**Tecnología para la Paz y la Soberanía Alimentaria**
