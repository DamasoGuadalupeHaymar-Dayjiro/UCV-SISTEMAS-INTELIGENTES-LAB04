import cv2
def analizar_imagen(path: str):
    imagen = cv2.imread(path, 0)
    if imagen is None:
        return {
            "error": "No se pudo cargar la imagen"
        }
    bordes = cv2.Canny(imagen, 50, 150)
    return {
        "alto": int(imagen.shape[0]),
        "ancho": int(imagen.shape[1]),
        "bordes_detectados": int(bordes.sum() > 0)
    }