from fastapi import FastAPI, UploadFile, File
import shutil
import os
from lab4_api_cv.services.image_service import analizar_imagen
app = FastAPI(
    title="Lab4 API CV",
    description="API de procesamiento de imágenes con FastAPI y OpenCV",
    version="1.0.0"
)
os.makedirs("data", exist_ok=True)
@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }
@app.post("/analyze-image")
def analyze_image(file: UploadFile = File(...)):
    ruta = f"data/{file.filename}"
    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    resultado = analizar_imagen(ruta)
    return {
        "mensaje": "Procesamiento exitoso",
        "archivo": file.filename,
        "resultado": resultado
    }