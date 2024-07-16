### Setup
1. Download and Install Python and VS Code
2. Create a virtual environment and install the requirements
3. Follow the steps below

    ### 1. **Basic Python Knowledge**
    - **Python Basics**: Ensure they understand basic Python syntax, functions, and imports.
    - **Modules and Packages**: Explain how to import and use modules and packages.

    ### 2. **Libraries and Tools Used**
    - **Joblib**: Used for loading machine learning models. Explain that `joblib` is often used for saving and loading complex models or large datasets because it is optimized for performance.
    - **Warnings**: The `warnings` module is used to control warning messages, which can help avoid unnecessary clutter in the console.
    - **FastAPI**: Introduce FastAPI as a modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
    - **Pydantic**: Mention that Pydantic (used indirectly here) helps with data validation in FastAPI through models like `StarInput`.

    ### 3. **Understanding the Code**

    #### Imports and Initial Setup
    ```python
    import joblib
    import warnings
    from fastapi import FastAPI
    from star_properties import StarInput
    from star_types_data import star_types
    ```
    - **Imports**: Explain each import and its purpose.
    - `joblib` for loading the ML model.
    - `warnings` to ignore warnings.
    - `FastAPI` for creating the API.
    - `StarInput` and `star_types` are custom modules/files that provide data models and mappings for star types.

    #### Ignoring Warnings
    ```python
    warnings.filterwarnings('ignore')
    ```
    - **Purpose**: To ignore warnings, often done to avoid cluttering the console with non-critical messages.

    #### Initialize FastAPI App
    ```python
    app = FastAPI()
    ```
    - **FastAPI Instance**: Create an instance of the FastAPI app, which will be used to define routes and handle requests.

    #### Load Model at Startup
    ```python
    pipeline = None

    @app.on_event("startup")
    def load_model():
        global pipeline
        pipeline_path = 'startype_pipeline.joblib'
        pipeline = joblib.load(pipeline_path)
        print("Model loaded successfully")
    ```
    - **Global Variable**: `pipeline` is declared globally to be accessible in other functions.
    - **Startup Event**: Use `@app.on_event("startup")` to ensure the model is loaded when the app starts, making it ready for predictions.
    - **Model Loading**: Load the machine learning model from a file using `joblib.load`.

    #### Root Endpoint
    ```python
    @app.get("/")
    def index_root():
        return {"App": "Running"}
    ```
    - **Root Endpoint**: Define a simple GET endpoint at the root ("/") that returns a JSON response indicating the app is running. This is useful for health checks.

    #### Prediction Endpoint
    ```python
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
    ```
    - **POST Endpoint**: Define a POST endpoint at "/predict" that takes `StarInput` data.
    - **Data Preparation**: Prepare the input data for the model in the required format.
    - **Prediction**: Use the loaded model to make a prediction and return the corresponding star type.

    ### 4. **Running the App**
    - **Start FastAPI**: Explain how to run the FastAPI app, typically using `uvicorn`.
    ```sh
    uvicorn script_name:app --reload
    ```

    ### 5. **Testing the API**
    - **Testing**: Show how to test the endpoints using a tool like `curl`, Postman, or FastAPI's interactive API docs available at `http://127.0.0.1:8000/docs`.

    ### Summary
    - The provided FastAPI application loads a pre-trained machine learning model at startup and exposes two endpoints: one for checking if the app is running and another for making predictions based on input data about stars.