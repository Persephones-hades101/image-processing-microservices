import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

SAVE_DIR = "storage/"

@app.get("/view/{filename}")
async def view_image(filename: str):
    """Retrieve and serve the stored image by filename."""
    file_path = os.path.join(SAVE_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/png")
    return JSONResponse(content={"error": "File not found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
