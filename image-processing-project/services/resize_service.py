import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image

router = APIRouter()

SAVE_DIR = "storage/"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure storage directory exists

@router.post("/resize/")
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
