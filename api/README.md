# Photo Caption API

The **Photo Caption API** generates a caption from an uploaded image.

## Features

- **Image Captioning**: Generates a caption for an uploaded image.

## Development

1. Install dependencies:

```bash
pip install fastapi uvicorn torch transformers fastai pillow
```

2. Run the API server:

```bash
uvicorn api.main:app --reload
```

3. Access the API at `http://localhost:8000`


## API Endpoints

- **Upload Image**: `POST /upload` - Uploads an image file (`multipart/form-data`) to generate a caption.

- **Health Check**: `GET /health` - Verifies API availability.

## Example

### Upload Image

```bash
curl -X POST "http://localhost:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@/path/to/your/image.jpg"
```

### Response

```json
{
    "detected_pet": "chiki",
    "confidence": 0.9998524188995361,
    "general_caption": "a dog laying on a blanket on the grass ",
    "refined_caption": "Chiki enjoying a sunny day on her blanket. Perfect spot for relaxation."
}
```


