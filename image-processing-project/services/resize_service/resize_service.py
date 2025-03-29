import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image

app = FastAPI()

SAVE_DIR = "storage/"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure storage directory exists

@app.post("/resize/")
async def resize_image(file: UploadFile = File(...), width: int = 200, height: int = 200):
    """Resize the uploaded image and save it."""
    try:
        image = Image.open(file.file)
        image = image.resize((width, height))

        save_path = os.path.join(SAVE_DIR, f"resized_{file.filename}")
        image.save(save_path, format="PNG")

        return JSONResponse(content={"filename": file.filename, "saved_path": save_path, "message": "Image resized successfully"})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
