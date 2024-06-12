# Breast Cancer Detection API

Esta es una API para la detección de cáncer de mama utilizando un modelo de aprendizaje profundo entrenado con Keras y TensorFlow. La API está implementada con FastAPI y se puede desplegar en Azure Web Services.

## Requisitos

- Python 3.7+
- Pipenv o virtualenv (opcional pero recomendado)
- Azure CLI (para el despliegue en Azure Web Services)

## Archivos

- `model.json`: La arquitectura del modelo en formato JSON.
- `model.keras`: Los pesos del modelo entrenado.
- `main.py`: El script de FastAPI para servir la API.

## Instalación y Configuración

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/breast-cancer-detection-api.git
cd breast-cancer-detection-api
```

### Paso 2: Crear un Entorno Virtual

Es recomendable usar un entorno virtual para manejar las dependencias. Puedes usar `virtualenv` o `pipenv`.

Con `virtualenv`:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

Con `pipenv`:

```bash
pipenv shell
```

### Paso 3: Instalar Dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

Asegúrate de que el archivo `requirements.txt` contiene las siguientes dependencias:

```bash
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

La API estará disponible en `http://127.0.0.1:8000/predict/`.

## Uso de la API

Puedes probar la API utilizando herramientas como `curl` o Postman.

### Ejemplo con `curl`

```bash
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@/ruta/a/tu/imagen.png"
```

### Ejemplo con Postman

1. Abre Postman.
2. Crea una nueva solicitud POST.
3. Ingresa `http://127.0.0.1:8000/predict/` como la URL.
4. Ve a la pestaña `Body`, selecciona `form-data`.
5. Añade una nueva clave con el nombre `file`, tipo `File`, y selecciona el archivo de imagen que deseas subir.
6. Haz clic en `Send` para enviar la solicitud y ver la respuesta.

## Despliegue en Azure Web Services

### Paso 1: Configurar Azure CLI

Asegúrate de tener la Azure CLI instalada y configurada. Si no la tienes, sigue las instrucciones en [Azure CLI Installation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

### Paso 2: Crear un Plan de Servicio y una Aplicación Web

```bash
az webapp up --name breast-cancer-detection-api --resource-group myResourceGroup --runtime "PYTHON:3.8"
```

### Paso 3: Desplegar la Aplicación

1. Empaqueta tus archivos en un archivo zip o usa el siguiente comando para desplegar desde el directorio actual:

```bash
az webapp up --name breast-cancer-detection-api --resource-group myResourceGroup --sku F1
```

### Paso 4: Configurar el Despliegue Continuo (Opcional)

Puedes configurar el despliegue continuo desde GitHub, Azure Repos, o cualquier otro sistema de control de versiones siguiendo las guías de Azure App Services.

## Notas

- Asegúrate de que los archivos `model.json` y `model.keras` estén en el mismo directorio que `main.py`.
- Ajusta el nombre del servicio de la web y el grupo de recursos según sea necesario.
- Asegúrate de tener permisos suficientes en tu cuenta de Azure para crear y gestionar recursos.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

### Archivos de Ejemplo

#### `main.py`

```python
from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from io import BytesIO
from PIL import Image

# Cargar el modelo
with open("model.json", "r") as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.keras")
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Inicializar FastAPI
app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Leer el archivo y convertirlo en un objeto BytesIO
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        image = image.resize((25, 25))
        image = img_to_array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        
        # Hacer la predicción
        prediction = loaded_model.predict(image)
        result = {
            "cancer_probability": str(round(prediction[0][1] * 100, 2)) + "%",
            "no_cancer_probability": str(round(prediction[0][0] * 100, 2)) + "%"
        }
        return result
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
