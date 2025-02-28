# 🐳 API de Estudiantes con Flask & PostgreSQL (Docker Compose)

Este proyecto es una **API en Flask** que gestiona datos de estudiantes, utilizando **PostgreSQL** como base de datos, todo en contenedores con **Docker Compose**.

## 🚀 Características
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para estudiantes.
- Persistencia de datos en **PostgreSQL** en lugar de JSON.
- Totalmente orquestado con **Docker Compose**.

---

## 🛠️ Instrucciones de Instalación

### 1️⃣ **Clonar el Repositorio**
```bash
git clone https://github.com/Pidual/Students.git
cd Students
```

### 2️⃣ **Crear el Archivo `.env`**  
Para que la base de datos funcione correctamente, debes crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```ini
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña
POSTGRES_DB=students_db
```

> ⚠ **Importante:** Reemplaza `tu_usuario` y `tu_contraseña` con los valores que desees.

### 3️⃣ **Ejecutar el Proyecto con Docker Compose**
```bash
docker compose up --build
```
- La **API** estará disponible en: `http://127.0.0.1:5000`
- La base de datos **PostgreSQL** se ejecutará en un contenedor.

### 4️⃣ **Probar la API**
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

---

## 📝 Licencia  
Este proyecto está bajo la **Licencia MIT**.  

---

## 🔗 Contacto  
Si tienes dudas o sugerencias, contáctame en **[tu_email@example.com]** o abre un issue en el repositorio.

---

### 🚀 **Contribuir al Proyecto**
Si deseas contribuir, sigue estos pasos:
1. **Haz un fork** del repositorio.
2. Crea una nueva rama:  
   ```bash
   git checkout -b feature-nueva-funcionalidad
   ```
3. Haz tus cambios y confirma los cambios:
   ```bash
   git add .
   git commit -m "Añadida nueva funcionalidad X"
   ```
4. Sube los cambios a tu fork:
   ```bash
   git push origin feature-nueva-funcionalidad
   ```
5. Abre un **Pull Request** en este repositorio.

---

## 📀 Subir los Cambios a GitHub  
Una vez que completes el `README.md`, súbelo a GitHub con estos comandos:
```bash
git add README.md
git commit -m "Añadido README.md con instrucciones"
git push origin main
```

🚀🔥 ¡Listo! Ahora tu proyecto tiene una documentación clara y profesional.

