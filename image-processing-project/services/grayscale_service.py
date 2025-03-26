import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image

router = APIRouter()

SAVE_DIR = "storage/"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure storage directory exists

@router.post("/grayscale/")
async def grayscale_image(file: UploadFile = File(...)):
    """Convert the uploaded image to grayscale and save it."""
    try:
        image = Image.open(file.file)
        grayscale_image = image.convert("L")  # Convert to grayscale

        save_path = os.path.join(SAVE_DIR, f"grayscale_{file.filename}")
        grayscale_image.save(save_path, format="PNG")

        return JSONResponse(content={"filename": file.filename, "saved_path": save_path, "message": "Image converted to grayscale successfully"})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
