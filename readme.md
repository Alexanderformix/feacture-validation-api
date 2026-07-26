# Feature Validación API

## 1.Descripción

Feature Validación API es una solución backend desarrollada con Django y Django REST Framework que permite la carga, almacenamiento y validación de documentos.

La aplicación implementa autenticación mediante JWT, almacenamiento de archivos en AWS S3 y un mecanismo configurable de asignación de responsables para la validación de documentos.

El sistema permite:

- Subir documentos.
- Asociarlos a un tipo de documento.
- Configurar responsables de validación.
- Generar tareas de validación.
- Aprobar o rechazar documentos.
- Notificar a los usuarios.
- Gestionar permisos mediante JWT.

## 2.Tecnologías utilizadas

- Django 6
- Django REST Framework
- Django Simple JWT
- AWS S3
- SQLite3
- Git
- GitHub
- Postman

## 3.Arquitectura del proyecto

users/
- Gestión de perfiles y roles.

documents/
- Gestión de documentos y tipos de documento.

validations/
- Reglas de validación y tareas de aprobación.

notifications/
- Notificaciones internas.

feature_validacion_api/
- Configuración principal del proyecto.

## 5.Flujo de validación

1. El usuario inicia sesión mediante JWT.
2. El usuario carga un documento.
3. El documento es almacenado en AWS S3.
4. El sistema consulta la configuración de ValidationRule.
5. Se crea una ValidationTask.
6. El responsable es notificado.
7. El responsable consulta sus tareas pendientes.
8. El responsable aprueba o rechaza el documento.
9. El estado del documento es actualizado.

## 6.Instalación

```bash
git clone https://github.com/Alexanderformix/feacture-validation-api.git

cd feacture-validation-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt 
```

## 7. VARIABLES DE ENTORNO

Crear un archivo `.env` utilizando el archivo `.env.example`.

Variables:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME
- AWS_S3_REGION_NAM

## 8.Ejecutar el proyecto

```bash
python manage.py migrate

python manage.py runserver
```

## 9.Ejecutar pruebas

```bash
python manage.py test
```

Salida esperada:

```text
Found 4 tests.

OK
```

## 10.Endpoints

### Usuarios

POST /api/users/login/

POST /api/users/refresh/

GET /api/users/profiles/

### Documentos

GET /api/documents/documents/

POST /api/documents/documents/

GET /api/documents/document-types/

### Validaciones

GET /api/validations/validation-rules/

GET /api/validations/validation-tasks/

POST /api/validations/validation-tasks/{id}/approve/

POST /api/validations/validation-tasks/{id}/reject/

### Notificaciones

GET /api/notifications/notifications/

## 11.Integración con AWS S3

Los archivos cargados son almacenados utilizando AWS S3 mediante django-storages.

La aplicación utiliza FileField junto con el backend:

storages.backends.s3.S3Storage

## 12.Decisiones técnicas

- Se utilizó JWT para autenticación.
- Se implementó AWS S3 para almacenamiento de documentos.
- Se diseñó ValidationRule para permitir la asignación dinámica de responsables.
- ValidationTask representa el proceso de aprobación.
- Notification permite implementar notificaciones internas.
- Se restringió la aprobación únicamente al usuario asignado.
- Se implementaron pruebas automatizadas utilizando Django TestCase.

## 13.Evidencia de pruebas

La solución fue validada utilizando:

- Postman.
- AWS S3.
- Django Admin.
- Django Test Framework.

## 14.Video demostración

https://youtu.be/enTPYZblDqI

## 15.Autor

Kevin Portela

Prueba técnica Backend
2026