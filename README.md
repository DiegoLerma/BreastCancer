# Breast Cancer Detection API

Esta es una API para la detección de cáncer de mama utilizando un modelo de aprendizaje profundo entrenado con Keras y TensorFlow. La API está implementada con FastAPI. 

## Requisitos

- Python 3.7+
- Pipenv (opcional pero recomendado)

## Archivos

- `model.json`: La arquitectura del modelo en formato JSON.
- `model.keras`: Los pesos del modelo entrenado.
- `main.py`: El script de FastAPI para servir la API.

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

## Notas

- Asegúrate de que los archivos `model.json` y `model.keras` estén en el mismo directorio que `main.py`.
- Ajusta el nombre del servicio de la web y el grupo de recursos según sea necesario.
- Asegúrate de tener permisos suficientes en tu cuenta de Azure para crear y gestionar recursos.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
