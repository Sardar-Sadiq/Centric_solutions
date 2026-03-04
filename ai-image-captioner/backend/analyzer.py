import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class CaptionGenerator:
    def __init__(self):
        # Loading the model (it might take a moment the first time)
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def generate(self, image_path):
        try:
            raw_image = Image.open(image_path).convert('RGB')
            # Process image for the model
            inputs = self.processor(raw_image, return_tensors="pt")
            
            # Generate caption
            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            
            return caption
        except Exception as e:
            return f"Error analyzing image: {str(e)}"