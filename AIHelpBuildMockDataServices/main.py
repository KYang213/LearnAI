from fastapi import FastAPI, HTTPException
import os
import json

app = FastAPI()

DATA_FOLDER = "data"

@app.get("/data/{filename}")
async def get_data(filename: str):
    file_path = os.path.join(DATA_FOLDER, f"{filename}.json")
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_path, "r") as file:
        data = json.load(file)

    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
