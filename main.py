from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import uvicorn
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

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Endpoint de health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}

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
    uvicorn.run(app, host="0.0.0.0", port=8000)
