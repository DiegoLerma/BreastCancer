# Breast Cancer Detection API

Esta API permite la detección de cáncer de mama en muestras histologicas mediante un modelo de aprendizaje profundo entrenado con Keras y TensorFlow. La API está implementada usando FastAPI.

## Requisitos

- Python 3.7+
- Pipenv (opcional, pero recomendado)

## Archivos del Proyecto

- `model.json`: Arquitectura del modelo en formato JSON.
- `model.keras`: Pesos del modelo entrenado.
- `main.py`: Script de FastAPI para servir la API.
- `requirements.txt`: Archivo con las dependencias necesarias.

El modelo fue entraenado previamente.  

## Instalación y Configuración

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/DiegoLerma/BreastCancer.git
cd breast-cancer-model
```

### Paso 2: Crear un Entorno Virtual

Es recomendable usar un entorno virtual para manejar las dependencias.

Con `pip`:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```txt
fastapi
uvicorn
tensorflow
pillow
```

### Paso 4: Ejecutar la API Localmente

Para ejecutar la API localmente, usa el siguiente comando:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Endpoints de la API

### Root Endpoint

- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Endpoint raíz para verificar que la API está activa.
- **Respuesta**: `{"message": "Hello World"}`

### Health Check Endpoint

- **URL**: `/health`
- **Método**: `GET`
- **Descripción**: Endpoint para verificar el estado de la API.
- **Respuesta**: `{"status": "ok"}`

### Predict Endpoint

- **URL**: `/predict/`
- **Método**: `POST`
- **Descripción**: Endpoint para realizar una predicción basada en una imagen de mamografía.
- **Parámetros**:
  - `file`: Imagen en formato multipart/form-data.
- **Respuesta**:

  ```json
  {
    "cancer_probability": "10.95%",
    "no_cancer_probability": "89.05%"
  }
  ```

- **Errores**:
  - `400`: `Invalid image file`
  - `500`: Mensaje detallado del error.

## Uso de la API

### Ejemplo con `curl`

```bash
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@/ruta/a/tu/imagen.png"
```

### Ejemplo con Postman

1. Abre Postman.
2. Crea una nueva solicitud `POST`.
3. Ingresa `http://127.0.0.1:8000/predict/` como la URL.
4. Ve a la pestaña `Body`, selecciona `form-data`.
5. Añade una nueva clave con el nombre `file`, tipo `File`, y selecciona el archivo de imagen que deseas subir.
6. Haz clic en `Send` para enviar la solicitud y ver la respuesta.

## Notas Importantes

- Asegúrate de que los archivos `model.json` y `model.keras` estén en el mismo directorio que `main.py`.
- La imagen debe tener un tamaño adecuado (se redimensionará a 25x25 píxeles).

## Contribuciones

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
