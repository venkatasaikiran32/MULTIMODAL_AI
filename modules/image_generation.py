import requests
from PIL import Image
from io import BytesIO
from modules.logger import logger
import os
import base64

API_KEY = os.getenv('OPENAI_API_KEY')
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_image(prompt):
    """Generate an image using Hugging Face API and return base64 string."""
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))

            # Convert image to base64
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

            logger.info("Image generated and encoded successfully")
            return img_base64
        else:
            logger.error(f"Error in image generation: {response.json()}")
            return None
    except Exception as e:
        logger.error(f"Image generation error: {str(e)}")
        return None

