# SatNet – Sistema de Asistencia Técnica

**SatNet** es una aplicación web desarrollada en Django para gestionar las operaciones del Departamento Técnico de mantenimiento en casinos. Centraliza el control de materiales, entregas, reparaciones de laboratorio y flujos de aprobación, eliminando el uso de papel y mejorando la trazabilidad de los procesos técnicos.

---

## 🚀 Funcionalidades Principales

### Inventario y Materiales
- Gestión de materiales alineados al índice del módulo MM de SAP.
- Registro y actualización de stock por parte del personal autorizado.
- Validaciones automáticas de existencia antes de realizar una entrega.

### Actas de Entrega (Laboratorio)
- Registro de entregas con múltiples ítems por acta.
- Soporte para materiales repetidos (modo “caja registradora”).
- Guardado automático de actas no firmadas para completar luego.
- Firma del técnico al finalizar la entrega.

### Flujos de Aprobación
- Módulo genérico reutilizable.
- Flujo por etapas: técnico → supervisor → seguridad → almacén.
- Control del estado de aprobación desde cada vista.

### Documentación y Reportes
- Generación de actas en PDF (WeasyPrint).
- Listado filtrable por técnico, estado y fecha.
- Dashboard con indicadores: entregas por mes, materiales más usados, técnicos activos.

---

## ⚙️ Tecnologías Utilizadas

- Python 3.12  
- Django 4.x  
- WeasyPrint (PDF)  
- Bootstrap 5  
- Gunicorn + Nginx (producción)  
- Base de datos: SQLite (desarrollo) / PostgreSQL (producción)

---

## 🗂 Estructura del Proyecto

```
SatNet/
├── config/              # Configuración Django
├── inventario/          # App principal (materiales, actas)
├── aprobaciones/        # App para flujo de aprobaciones
├── templates/           # HTML por app (base, actas, login, etc.)
├── static/              # CSS y JS
├── media/               # PDFs y archivos generados
├── requirements.txt     # Dependencias del proyecto
└── README.md
```

---

## 💻 Instalación (Entorno de Desarrollo)

```bash
git clone https://github.com/babuenop/SatNet.git
cd SatNet
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Accede a la app desde: http://127.0.0.1:8000/

---

## 📌 Próximos Desarrollos

- Control de roles y permisos por grupo (técnico, supervisor, almacén).
- Firma electrónica avanzada.
- Notificaciones por cambio de estado o faltantes de stock.
- Dashboard por usuario y filtros personalizados.
- Digitalización de ingreso y egreso en almacén físico.

---

## 👤 Autor

Proyecto desarrollado por **babuenop**,  


---

## 📝 Licencia

Free