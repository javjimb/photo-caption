from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from ..utils.logging_config import configure_logging
from ..services.caption_generation import CaptionGenerator
from ..services.pet_classifier import PetClassifier
from ..services.caption_refiner import CaptionRefiner
from PIL import Image as PILImage, UnidentifiedImageError
import io
import torch
import warnings

logger = configure_logging()
router = APIRouter()

device = "cuda" if torch.cuda.is_available() else "cpu"

# Suppress specific warning
warnings.filterwarnings("ignore", message="`resume_download` is deprecated and will be removed in version 1.0.0.")

# Load models
models_dir = Path(__file__).resolve().parents[2] / "models"

# Initialize services
pet_classifier = PetClassifier(models_dir / 'fastai_resnet18_pet_classifier_20240604.pkl')
caption_generator = CaptionGenerator("nlpconnect/vit-gpt2-image-captioning", device)
caption_refiner = CaptionRefiner(models_dir / "gpt2_alpaca_preprocess_fn_custom/best_model", device)


@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename}")

        # Read the image file
        # image_bytes = await file.read()
        # img = PILImage.open(io.BytesIO(image_bytes))

        image_bytes = await file.read()
        
        if not image_bytes:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        try:
            img = PILImage.open(io.BytesIO(image_bytes)).convert("RGB")
        except UnidentifiedImageError:
            raise HTTPException(status_code=400, detail="Uploaded file is not a valid image")
        
        if img is None:
            raise HTTPException(status_code=400, detail="Failed to process the uploaded image")


        # Make prediction
        pred_class, pred_idx, outputs = pet_classifier.predict(img)
        logger.info(f"Predicted class: {pred_class}, confidence: {outputs[pred_idx].item()}")

        # Generate caption
        caption = caption_generator.generate_caption(img)
        logger.info(f"Generated caption: {caption}")

        # Refine caption
        refined_caption = caption_refiner.refine_caption(str(pred_class), caption)
        logger.info(f"Generated refined caption: {refined_caption}")

        # Prepare response
        response = {
            "detected_pet": str(pred_class),
            "confidence": outputs[pred_idx].item(),
            "general_caption": caption,
            "refined_caption": refined_caption
        }
        return JSONResponse(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))