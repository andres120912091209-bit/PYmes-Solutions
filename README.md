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

# Pymes Solutions API

Backend del sistema **Pymes Solutions**, una aplicación orientada a la gestión de Pequeñas y Medianas Empresas (Pymes).  
Este proyecto implementa los módulos principales de **Clientes** y **Productos** utilizando una arquitectura en capas con Spring Boot.

## Descripción del proyecto

Pymes Solutions permite administrar la información de clientes y productos de una Pyme de forma eficiente.  
El sistema fue desarrollado aplicando principios de Programación Orientada a Objetos, persistencia de datos con JPA y buenas prácticas de desarrollo de software.

## Módulos desarrollados

### Módulo Clients (Clientes)
- Crear cliente
- Listar clientes
- Consultar cliente por ID
- Actualizar cliente
- Eliminar cliente

### Módulo Products (Productos)
- Crear producto
- Listar productos
- Consultar producto por ID
- Actualizar producto
- Eliminar producto

## Tecnologías utilizadas

- **Lenguaje:** Java 21
- **Framework:** Spring Boot 4
- **Persistencia:** Spring Data JPA + Hibernate
- **Base de datos:** H2 (en memoria)
- **Arquitectura:** Capas (Model, Repository, Service, Controller)
- **Control de versiones:** Git + GitHub
- **Herramientas:** IntelliJ IDEA, Maven, Postman

## Estructura del proyecto

com.pymessolutions.pymes_solutions
├── model          → Entidades (Client, Product)
├── repository     → Acceso a datos
├── service        → Lógica de negocio
├── controller     → Endpoints REST
└── PymesSolutionsApplication.java


## Cómo ejecutar el proyecto

### Requisitos
- JDK 17 o 21
- Maven
- IntelliJ IDEA (recomendado)

### Pasos
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/pymes-solutions.git
Abrir el proyecto en IntelliJ IDEA
Ejecutar la clase PymesSolutionsApplication
La API estará disponible en:
http://localhost:8080

Consola de base de datos H2

URL: http://localhost:8080/h2-console
JDBC URL: jdbc:h2:mem:pymesdb
Usuario: sa
Contraseña: (vacía)

Endpoints principales
Clients

MétodoEndpointDescripciónGET/api/v1/clientsListar todos los clientesGET/api/v1/clients/{id}Obtener cliente por IDPOST/api/v1/clientsCrear clientePUT/api/v1/clients/{id}Actualizar clienteDELETE/api/v1/clients/{id}Eliminar cliente
Products


MétodoEndpointDescripciónGET/api/v1/productsListar todos los productosGET/api/v1/products/{id}Obtener producto por IDPOST/api/v1/productsCrear productoPUT/api/v1/products/{id}Actualizar productoDELETE/api/v1/products/{id}Eliminar producto
Autor
Andrés Camilo

Proyecto formativo – Ingeniería de Tecnologías de la Información y la Comunicación

SENA / ITC


---

### Cómo guardarlo

1. En IntelliJ busca el archivo `README.md` (está en la raíz del proyecto)
2. Si no existe, créalo: clic derecho en la raíz del proyecto → **New → File** → nómbralo `README.md`
3. Pega el contenido de arriba
4. Guarda el archivo
5. Haz commit:

```powershell
git add README.md
git commit -m "docs: update README with project information"
git push
