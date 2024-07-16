# Imports
import joblib
import warnings
from fastapi import FastAPI
from star_properties import StarInput
from star_types_data import star_types

# Ignore the warnings due to version changes
warnings.filterwarnings('ignore')

# Initialize the FastAPI app
app = FastAPI()

# Load the pipeline as a global variable
pipeline = None

# Define the startup event to load the model when the app starts
@app.on_event("startup")
def load_model():
    global pipeline
    pipeline_path = 'startype_pipeline.joblib'
    pipeline = joblib.load(pipeline_path)
    print("Model loaded successfully")

# Define the Index root
@app.get("/")
def index_root():
    return {"App": "Running"}

# Define the prediction endpoint
@app.post("/predict")
async def prediction(input_data: StarInput):
    # Input Data for the pipeline
    data = [[
        input_data.temperature,
        input_data.luminosity,
        input_data.radius,
        input_data.absolute_magnitude
    ]]

    # Make Prediction
    prediction = pipeline.predict(data)[0]

    return {'Predicted Star Type': star_types[prediction]}
