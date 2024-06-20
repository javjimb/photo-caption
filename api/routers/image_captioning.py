from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # TODO: Add image captioning logic here
    return JSONResponse({"dog": "Chiki", "caption": "Chiki enjoying a sunny day."})