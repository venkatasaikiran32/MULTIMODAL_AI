
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
from modules.logger import logger

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def match_image_keywords(image_file, keywords):
    """Matches an uploaded image with provided keywords and returns similarity scores."""
    try:
        # Load image from file-like object
        image = Image.open(image_file).convert("RGB")

        # Split keyword string into list
        if isinstance(keywords, str):
            keywords = [kw.strip() for kw in keywords.split(",") if kw.strip()]

        # Process inputs through CLIP
        inputs = clip_processor(text=keywords, images=image, return_tensors="pt", padding=True)
        outputs = clip_model(**inputs)

        # Extract scores
        similarity_scores = outputs.logits_per_image[0].tolist()
        results = {keywords[i]: similarity_scores[i] for i in range(len(keywords))}

        logger.info("CLIP image-keyword matching successful.")
        return results, similarity_scores

    except Exception as e:
        logger.error(f"CLIP error: {str(e)}")
        return None, []
