import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image

app = FastAPI()

SAVE_DIR = "/app/storage/"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure storage directory exists


@app.post("/grayscale/")
async def grayscale_image(file: UploadFile = File(...)):
    """Convert the uploaded image to grayscale and save it."""
    try:
        image = Image.open(file.file)
        grayscale_image = image.convert("L")  # Convert to grayscale
        save_path = os.path.join(SAVE_DIR, f"grayscale_{file.filename}")

        print(f"About to save file to: {save_path}")
        print(f"Absolute path: {os.path.abspath(save_path)}")

        grayscale_image.save(save_path, format="PNG")

        print(f"File saved successfully: {save_path}")

        return JSONResponse(content={"filename": file.filename, "saved_path": save_path, "message": "Image converted to grayscale successfully"})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
