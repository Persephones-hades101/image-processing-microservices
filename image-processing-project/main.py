from fastapi import FastAPI
from services.grayscale_service.grayscale_service import router as grayscale_router
from services.resize_service.resize_service import router as resize_router
from services.view_service.view_service import router as view_router


app = FastAPI()

# Register the microservices
app.include_router(resize_router, prefix="/image", tags=["Image Processing"])
app.include_router(grayscale_router, prefix="/image", tags=["Image Processing"])
app.include_router(view_router, prefix="/image", tags=["Image Viewing"])

@app.get("/")
def read_root():
    return {"message": "Image Processing API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
