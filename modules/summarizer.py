from transformers import pipeline
from modules.logger import logger

# Specify the summarization model explicitly
MODEL_NAME = "facebook/bart-base"  # Base model for summarization

logger.info(f"Loading summarization model: {MODEL_NAME}...")
summarizer = pipeline("summarization", model=MODEL_NAME)

def summarize_text(text, max_length=150, min_length=50):
    """Summarize text using Hugging Face summarization model."""
    if not text.strip():
        logger.warning("Empty text provided for summarization.")
        return "No text provided."

    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        logger.info("Summarization successful.")
        return summary[0]['summary_text']
    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        return "Error summarizing text."

if __name__ == "__main__":
    example_text = "Artificial Intelligence (AI) is a branch of computer science ..."
    print("Summary:", summarize_text(example_text))







