````md
# UCV - Sistemas Inteligentes - Laboratorio 04

## API de Visión por Computadora con FastAPI y OpenCV

Proyecto desarrollado para la Guía de Práctica N.° 4 del curso **Sistemas Inteligentes**, enfocado en la construcción de una API para procesamiento de imágenes utilizando FastAPI, OpenCV, Poetry y una estructura modular inspirada en Kedro.

---

# 📘 Descripción del Proyecto

Esta aplicación permite recibir imágenes mediante una API REST, procesarlas con técnicas básicas de visión por computadora y devolver resultados estructurados en formato JSON.

La funcionalidad principal consiste en:

- Subida de imágenes
- Lectura de imágenes con OpenCV
- Conversión a escala de grises
- Detección de bordes con algoritmo Canny
- Respuesta estructurada con dimensiones y análisis

---

# 🎯 Objetivo

Construir una API capaz de procesar imágenes aplicando detección de bordes y devolver resultados estructurados, integrando:

- FastAPI
- OpenCV
- Poetry
- Programación modular

---

# 🛠 Tecnologías Utilizadas

- Python 3.12
- Poetry
- FastAPI
- Uvicorn
- OpenCV
- NumPy
- Pytest

---

# 📂 Estructura del Proyecto

```text
lab4_api_cv/
│── pyproject.toml
│── poetry.lock
│── README.md
│── .gitignore
│── data/
│── src/
│   └── lab4_api_cv/
│       ├── __init__.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── main.py
│       └── services/
│           ├── __init__.py
│           └── image_service.py
└── tests/
    └── test_api.py
````

---

# ⚙ Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/DamasoGuadalupeHaymar-Dayjiro/UCV-SISTEMAS-INTELIGENTES-LAB04.git
cd UCV-SISTEMAS-INTELIGENTES-LAB04
```

---

## 2. Instalar dependencias

```bash
poetry install
```

---

## 3. Activar entorno virtual

### Windows CMD:

```bash
.venv\Scripts\activate
```

### PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

---

# ▶ Ejecución de la API

```bash
poetry run uvicorn lab4_api_cv.api.main:app --reload
```

---

# 🌐 Documentación Interactiva (Swagger)

Una vez ejecutado:

```text
http://127.0.0.1:8000/docs
```

---

# 📌 Endpoints Disponibles

## GET /

Verifica que la API funciona correctamente.

### Respuesta:

```json
{
  "mensaje": "API funcionando correctamente"
}
```

---

## POST /analyze-image

Permite subir una imagen para procesarla.

### Parámetro:

* file (imagen .jpg / .png)

### Respuesta:

```json
{
  "mensaje": "Procesamiento exitoso",
  "resultado": {
    "alto": 720,
    "ancho": 1280,
    "bordes_detectados": 1
  }
}
```

---

# 🧠 Funcionamiento Interno

## Flujo del sistema:

1. Usuario sube imagen
2. FastAPI recibe archivo
3. Se guarda en carpeta `data/`
4. OpenCV carga la imagen
5. Se aplica detección de bordes con `cv2.Canny()`
6. Se devuelve resultado JSON

---

# 📷 Procesamiento de Imagen

## Archivo:

`src/lab4_api_cv/services/image_service.py`

### Funcionalidades:

* Lectura de imagen
* Escala de grises
* Detección de bordes
* Análisis de dimensiones

---

# 🧪 Pruebas

Ejecutar pruebas:

```bash
poetry run pytest
```

### Resultado esperado:

```text
1 passed
```

---

# 📊 Ejemplo de Código Principal

## image_service.py

```python
import cv2

def analizar_imagen(path: str):
    imagen = cv2.imread(path, 0)

    if imagen is None:
        return {"error": "No se pudo cargar la imagen"}

    bordes = cv2.Canny(imagen, 50, 150)

    return {
        "alto": imagen.shape[0],
        "ancho": imagen.shape[1],
        "bordes_detectados": int(bordes.sum() > 0)
    }
```

---

# 📚 Aprendizajes Obtenidos

* Desarrollo de APIs con FastAPI
* Uso de OpenCV para visión por computadora
* Gestión profesional de proyectos con Poetry
* Modularización de proyectos
* Integración entre backend y procesamiento de imágenes

---

# 🚀 Posibles Mejoras Futuras

* Detección facial
* Clasificación de imágenes con IA
* Guardado de imágenes procesadas
* Uso de Programación Orientada a Objetos
* Integración completa con Kedro pipelines

---

# 👨‍💻 Autor

**Damaso Guadalupe Haymar Dayjiro**
Estudiante de Ingeniería de Sistemas
Universidad César Vallejo

---

# 📄 Curso

**Sistemas Inteligentes**
Guía de Práctica N.° 4
API de Visión por Computadora con FastAPI y Kedro

---

# 🏁 Estado del Proyecto

## ✅ Proyecto funcional y operativo

* API implementada
* Procesamiento de imágenes
* Swagger habilitado
* GitHub configurado
* Entregable académico completo

```
```
