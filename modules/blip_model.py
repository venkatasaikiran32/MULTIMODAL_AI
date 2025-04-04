
# modules/blip_model.py

import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from modules.logger import logger

logger.info("Loading BLIP base model...")
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

def generate_caption(image_file, prompt=None):
    """Generate caption or visual question answering based on prompt."""
    image = Image.open(image_file).convert("RGB")
    inputs = processor(image, text=prompt if prompt else "a photo of", return_tensors="pt").to(device)

    output_ids = model.generate(**inputs)
    result = processor.decode(output_ids[0], skip_special_tokens=True)

    logger.info(f"BLIP Result: {result}")
    return result

