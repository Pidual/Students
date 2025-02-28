# 🐳 API de Estudiantes con Flask & PostgreSQL (Docker Compose)

Este proyecto es una **API en Flask** que gestiona datos de estudiantes, utilizando **PostgreSQL** como base de datos, todo en contenedores con **Docker Compose**.

## 🚀 Características
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para estudiantes.
- Orquestado con **Docker Compose**.

---

## 🛠️ Instrucciones de Instalación

### 1️ **Clonar el Repositorio**
```bash
git clone https://github.com/Pidual/Students.git
cd Students
```

### 2 **Ejecutar el Proyecto con Docker Compose**
```bash
docker compose up --build
```
- La **API** estará disponible en: `http://127.0.0.1:5000`
- La base de datos **PostgreSQL** se ejecutará en un contenedor.

### 3 **Probar la API**
Para verificar que todo funciona correctamente, usa:
```bash
curl http://127.0.0.1:5000/students
```
Si prefieres Postman, puedes hacer una petición **GET** a `http://127.0.0.1:5000/students`.

---

## 📚 Endpoints de la API

| Método | Endpoint      | Descripción               |
|--------|--------------|---------------------------|
| GET    | `/students`  | Obtener todos los estudiantes |
| POST   | `/students`  | Agregar un nuevo estudiante |
| PUT    | `/students`  | Actualizar un estudiante  |
| DELETE | `/students`  | Eliminar un estudiante    |

### 📌 **Ejemplo de Datos para `POST` o `PUT`**
Cuando hagas una petición `POST` o `PUT`, envía un JSON con este formato:
```json
{
    "nombre": "Carlos Pérez",
    "edad": 22,
    "carrera": "Ingeniería en Sistemas"
}
```

---

## 🛑 Detener los Contenedores  
Para detener la ejecución de los contenedores, usa:
```bash
docker compose down
```




