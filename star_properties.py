from pydantic import BaseModel

# Define the input data model
class StarInput(BaseModel):
    temperature: int
    luminosity: float
    radius: float
    absolute_magnitude: float