from fastapi import FastAPI
from api.routers import image_captioning

app = FastAPI()

app.include_router(image_captioning.router)