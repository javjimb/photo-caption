from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class CaptionRefiner:
    def __init__(self, model_name: str, device: str):
        self.device = device
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name).to(device)

    def refine_caption(self, pet_name: str, general_caption: str) -> str:
        # Construct the prompt for the model
        prompt = f"Pet: {pet_name}\nCaption: {general_caption}\nRefined Caption:"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        # Generate refined caption
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=100,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            num_beams=5,
            early_stopping=True
        )

        refined_caption = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return refined_caption
