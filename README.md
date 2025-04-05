# 🌐 Django RESTful Web Service

Este repositorio contiene un proyecto de backend desarrollado con **Django** y **Django REST Framework**, que expone una API RESTful modular, escalable y segura. Está pensado como una base sólida para construir sistemas robustos que manejen autenticación, permisos, versionado y consumo eficiente de datos.

## ⚙️ Tecnologías utilizadas

- **Python 3.11+**  
- **Django 5.x**  
- **Django REST Framework**  
- **PostgreSQL / SQLite**  
- **pytest / unittest** para pruebas  

## 🧩 Características principales

- CRUD completo sobre modelos personalizados  
- Autenticación con token
- Permisos personalizados  
- Versionado de API  
- Buenas prácticas RESTful  
- Estructura organizada y escalable  

## 🚀 Instalación y ejecución

1. Clonar el repositorio  
```bash
git clone https://github.com/franciscapr/django_restful_web_services.git
```

2. Crear entorno virtual e instalar dependencias  
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Aplicar migraciones y levantar el servidor  
```bash
python manage.py migrate
python manage.py runserver
```

## 📌 Notas

Este proyecto sigue principios de diseño limpios y desacoplados. La idea es que pueda escalarse fácilmente, integrarse con frontend (React, Vue, etc.) o adaptarse a microservicios.

---
![Api Browser - Root](https://raw.githubusercontent.com/franciscapr/django_restful_web_services/main/restful01/img/Captura%20desde%202025-04-05%2012-25-24.png)

![Api Browser - DroneCategoryList](https://raw.githubusercontent.com/franciscapr/django_restful_web_services/main/restful01/img/Captura%20desde%202025-04-05%2012-25-45.png)

