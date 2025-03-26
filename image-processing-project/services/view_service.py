import os
from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter()

SAVE_DIR = "storage/"

@router.get("/view/{filename}")
async def view_image(filename: str):
    """Retrieve and serve the stored image by filename."""
    file_path = os.path.join(SAVE_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/png")
    return JSONResponse(content={"error": "File not found"}, status_code=404)
