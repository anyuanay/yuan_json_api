from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

import json
from typing import Any

app = FastAPI()

# Assuming 'nobelprize-laureate.json' is in the same directory as this script
json_file_path = 'nobelprize-laureate.json'

# Endpoint to serve the JSON data
@app.get("/nobelprize/laureates")
async def read_laureates():
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data

# Define a Pydantic model for the structure of the laureates, if needed
class Laureate(BaseModel):
    id: str
    firstname: str
    surname: str
    # Include other fields as per the JSON structure

# If you want to serve the API on the internet, you would need to deploy it
# For local testing, run the server with uvicorn:
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
