from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from modules.logger import logger

# Load the pre-trained model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

chat_history = []  # Store previous conversations

def chatbot_response(user_input):
    """Generates chatbot responses while maintaining chat history"""
    try:
        chat_history.append(f"You: {user_input}")
        context = " ".join(chat_history[-5:])  # Keep last 5 exchanges

        inputs = tokenizer(context, return_tensors="pt")
        response_ids = model.generate(**inputs)
        bot_response = tokenizer.decode(response_ids[0], skip_special_tokens=True)

        chat_history.append(f"Chatbot: {bot_response}")
        logger.info("Chatbot generated response successfully")
        return bot_response
    except Exception as e:
        logger.error(f"Error in chatbot response: {str(e)}")
        return "Error generating response."

if __name__ == "__main__":
    while True:
        user_text = input("You: ")
        if user_text.lower() == "exit":
            break
        print("Bot:", chatbot_response(user_text))


