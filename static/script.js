async function recognizeSpeech() {
    let audioFile = document.getElementById("audioInput").files[0];
    let formData = new FormData();
    formData.append("audio", audioFile);

    let response = await fetch("/speech_to_text", { method: "POST", body: formData });
    let data = await response.json();
    document.getElementById("speechOutput").innerText = data.text;
}

async function sendMessage() {
    let userInput = document.getElementById("chatInput").value;
    let response = await fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });
    let data = await response.json();
    document.getElementById("chatOutput").innerText = data.response;
}

async function summarizeText() {
    let textInput = document.getElementById("textInput").value;
    let response = await fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: textInput })
    });
    let data = await response.json();
    document.getElementById("summaryOutput").innerText = data.summary;
}

async function generateImage() {
    let prompt = document.getElementById("imagePrompt").value;
    let response = await fetch("/generate_image", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt })
    });
    let data = await response.json();
    document.getElementById("generatedImage").src = "data:image/png;base64," + data.image;
    document.getElementById("generatedImage").style.display = "block";
}

// CLIP Image Matching
async function findBestMatch() {
    const imageFile = document.getElementById("clipImageInput").files[0];
    const keywords = document.getElementById("clipKeywords").value;
    const formData = new FormData();

    formData.append("image", imageFile);
    formData.append("keywords", keywords);

    try {
        const response = await fetch("/clip_match", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        if (data.best_match) {
            document.getElementById("clipOutput").innerText = data.best_match;
        } else {
            document.getElementById("clipOutput").innerText = "Error: " + (data.error || "Unknown error.");
        }

    } catch (err) {
        console.error("Request failed", err);
        document.getElementById("clipOutput").innerText = "Request failed. Check console for details.";
    }
}


// BLIP Model (Image Captioning / Visual QA)
async function blipProcess() {
    let imageFile = document.getElementById("blipImageInput").files[0];
    let prompt = document.getElementById("blipPrompt").value;
    let formData = new FormData();
    formData.append("image", imageFile);
    formData.append("prompt", prompt);

    let response = await fetch("/blip_caption", { method: "POST", body: formData });
    let data = await response.json();
    document.getElementById("blipOutput").innerText = data.caption;
}

