import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image, ImageFilter

app = FastAPI()

SAVE_DIR = "/app/storage/"
os.makedirs(SAVE_DIR, exist_ok=True)


@app.post("/filter/")
async def filter_image(file: UploadFile = File(...), filter_type: str = "blur"):
    """Apply filter to the uploaded image and save it."""
    print(filter_type)
    try:
        image = Image.open(file.file)

        # Apply the selected filter
        if filter_type == "blur":
            filtered_image = image.filter(ImageFilter.BLUR)
        elif filter_type == "contour":
            filtered_image = image.filter(ImageFilter.CONTOUR)
        elif filter_type == "emboss":
            filtered_image = image.filter(ImageFilter.EMBOSS)
        elif filter_type == "sharpen":
            filtered_image = image.filter(ImageFilter.SHARPEN)
        else:
            return JSONResponse(content={"error": "Invalid filter type"}, status_code=400)

        save_path = os.path.join(SAVE_DIR, f"{filter_type}_{file.filename}")
        print(f"About to save file to: {save_path}")
        print(f"Absolute path: {os.path.abspath(save_path)}")

        filtered_image.save(save_path, format="PNG")

        print(f"File saved successfully: {save_path}")

        return JSONResponse(content={
            "filename": file.filename,
            "saved_path": save_path,
            "message": f"Image processed with {filter_type} filter successfully"
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
