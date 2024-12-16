import joblib
import os
import cv2
import numpy as np

def cargar_modelo():
    """
    Carga el modelo de clasificación desde un archivo `.pkl`.

    Intenta cargar el modelo previamente entrenado almacenado en el archivo 'faces.pkl'.
    Si el archivo no se encuentra o ocurre un error durante la carga, se captura y se maneja
    el error, devolviendo None.

    Returns:
        modelo: El modelo cargado desde el archivo o None si ocurre un error.
    """
    try:
        modelo = joblib.load('./recursos/modelos/faces.pkl')
        return modelo
    except FileNotFoundError:
        print("Error: No se encontró el archivo del modelo 'faces.pkl'. Asegúrate de que el archivo esté en el directorio correcto.")
        return None
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

def cargar_imagen(nombre_archivo):
    """
    Carga una imagen desde un archivo y la convierte a escala de grises.

    Esta función verifica si el archivo existe y si puede ser leído correctamente como una imagen en escala de grises.
    Si no se puede cargar la imagen, devuelve None.

    Args:
        nombre_archivo (str): El nombre del archivo de imagen a cargar.

    Returns:
        np.ndarray: La imagen cargada en formato de escala de grises, o None si ocurre un error.
    """
    if not os.path.isfile(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no existe. Intenta de nuevo.")
        return None
    
    try:
        # Cargar la imagen en escala de grises en caso de que no lo este ya
        imagen = cv2.imread(nombre_archivo, cv2.IMREAD_GRAYSCALE)
        if imagen is None:
            print(f"Error: No se pudo leer la imagen '{nombre_archivo}'.")
            return None
        return imagen
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None

def preprocesar_imagen(imagen):
    """
    Preprocesa la imagen para la predicción.

    La imagen se redimensiona a un tamaño de 64x64 píxeles, se normalizan los valores de los píxeles 
    al rango [0, 1] y se aplanan en un vector de 4096 elementos para ser compatible con el modelo.

    Args:
        imagen (np.ndarray): La imagen en escala de grises a preprocesar.

    Returns:
        np.ndarray: La imagen transformada en un vector de 4096 elementos listos para la predicción.
    """
    # Redimensionar la imagen a 64x64 píxeles no pasa nada si ya lo esta
    imagen_redimensionada = cv2.resize(imagen, (64, 64))
    
    # Normalizar los valores de los píxeles (rango 0-1)
    imagen_normalizada = imagen_redimensionada / 255.0
    
    # Aplanar la imagen a un vector de 4096 elementos (Como en el csv entregado)
    imagen_vector = imagen_normalizada.flatten()
    
    return imagen_vector

def predecir():
    """
    Solicita un archivo de imagen, lo preprocesa y utiliza el modelo cargado para hacer una predicción.

    La función cargará el modelo desde un archivo 'faces.pkl', solicitará al usuario que ingrese 
    el nombre de un archivo de imagen, lo preprocesará y luego realizará una predicción con el modelo.
    Imprime el resultado de la predicción (el clúster al que pertenece la imagen) o un mensaje de error si ocurre algún problema.

    Returns:
        None
    """
    # Cargar el modelo
    modelo = cargar_modelo()
    if modelo is None:
        return
    
    # Solicitar el nombre del archivo de la imagen hasta que sea válido
    while True:
        nombre_imagen = input("Introduce el nombre del archivo de la imagen que deseas predecir: ")
        imagen = cargar_imagen(nombre_imagen)
        if imagen is not None:
            break
    
    # Preprocesar la imagen (normalización, redimensionamiento y aplanado)
    try:
        imagen_vector = preprocesar_imagen(imagen)
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return

    # Realizar la predicción
    try:
        prediccion = modelo.predict([imagen_vector])
        print(f"La imagen pertenece al clúster: {prediccion[0]}")
    except Exception as e:
        print(f"Error durante la predicción: {e}")

# Ejecutar la función de predicción
if __name__ == "__main__":
    predecir()
