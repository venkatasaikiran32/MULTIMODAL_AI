from flask import Flask, render_template, request, jsonify
from modules.speech_recognition import transcribe_audio
from modules.chatbot import chatbot_response
from modules.summarizer import summarize_text
from modules.image_generation import generate_image
from modules.clip_model import match_image_keywords
from modules.blip_model import generate_caption

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/speech_to_text", methods=["POST"])
def speech_to_text():
    return jsonify({"text": transcribe_audio(request.files["audio"])})

@app.route("/chatbot", methods=["POST"])
def chatbot():
    return jsonify({"response": chatbot_response(request.json["message"])})

@app.route("/summarize", methods=["POST"])
def summarize():
    return jsonify({"summary": summarize_text(request.json["text"])})

@app.route("/generate_image", methods=["POST"])
def generate():
    return jsonify({"image": generate_image(request.json["prompt"])})


@app.route("/clip_match", methods=["POST"])
def clip_match():
    image = request.files["image"]
    keywords = request.form["keywords"]
    results, scores = match_image_keywords(image, keywords)

    if results:
        best_keyword = max(results, key=results.get)
        return jsonify({
            "best_match": f"Best match: {best_keyword}",
            "scores": results
        })
    else:
        return jsonify({
            "error": "CLIP model failed to process input."
        }), 500


@app.route("/blip_caption", methods=["POST"])
def blip_caption():
    image = request.files["image"]
    prompt = request.form.get("prompt", "")  # optional prompt
    caption = generate_caption(image, prompt if prompt.strip() else None)
    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,threaded=True)






