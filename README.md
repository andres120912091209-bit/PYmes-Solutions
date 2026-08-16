# PYmes Solutions
“Proyecto formativo de control de versiones*
Push: Cambio en el archivo read me
Pull: CAmbio desde la web
Pegar o resumir las partes más importantes del README:

Descripción del proyecto
Pymes Solutions es una API backend desarrollada para la gestión de Pequeñas y Medianas Empresas. El sistema permite administrar clientes y productos de manera eficiente, aplicando una arquitectura en capas y principios de programación orientada a objetos.
Tecnologías utilizadas

Lenguaje: Python
Framework: FastAPI
ORM: SQLAlchemy
Validación de datos: Pydantic
Base de datos: SQLite
Control de versiones: Git y GitHub

Módulos desarrollados

Módulo Clients: Permite crear, listar, consultar, actualizar y eliminar clientes.
Módulo Products: Permite crear, listar, consultar, actualizar y eliminar productos, además de gestionar el stock.

Instrucciones de instalación y ejecución

Clonar el repositorio o descargar el proyecto.
Crear y activar un entorno virtual:
python -m venv venv
.\venv\Scripts\Activate
Instalar las dependencias:
pip install -r requirements.txt
Ejecutar la aplicación:
uvicorn app.main:app --reload
Abrir en el navegador:
http://127.0.0.1:8000/docs
