from fastai.vision.all import load_learner
from pathlib import Path

class PetClassifier:
    def __init__(self, model_path: Path):
        self.model = load_learner(model_path)

    def predict(self, img):
        return self.model.predict(img)
