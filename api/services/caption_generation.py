from transformers import VisionEncoderDecoderModel, GPT2TokenizerFast, ViTImageProcessor

class CaptionGenerator:
    def __init__(self, model_name: str, device: str):
        self.device = device
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name).to(device)
        self.tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
        self.image_processor = ViTImageProcessor.from_pretrained(model_name)

    def generate_caption(self, img, max_new_tokens: int = 50):
        try: 
            
          inputs = self.image_processor(images=img, return_tensors="pt").to(self.device)
          output = self.model.generate(
              pixel_values=inputs.pixel_values,
              max_new_tokens=max_new_tokens
          )

          if output.dim() == 2:
              output = output[0]

          caption = self.tokenizer.decode(output, skip_special_tokens=True)
          return caption

        except Exception as e:
            raise Exception(f"Failed to generate caption: {str(e)}")

