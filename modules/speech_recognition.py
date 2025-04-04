import whisper
import os
from modules.logger import logger

# Load the Whisper model
model = whisper.load_model("base")

def transcribe_audio(audio_file):
    """Transcribes speech from an uploaded audio file using Whisper"""
    try:
        if hasattr(audio_file, "save"):  # Check if it's a Flask FileStorage object if it then it temporarly stores that audio 
            temp_path = "temp_audio.mp3"
            audio_file.save(temp_path)  # Save the file
            audio_path = temp_path
        else:
            audio_path = audio_file  # Assume it's a valid file path

        logger.info(f"Processing audio: {audio_path}")
        result = model.transcribe(audio_path)
        transcription = result["text"]
        logger.info("Transcription completed successfully")

        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return transcription
    except Exception as e:
        logger.error(f"Error in transcribing audio: {str(e)}")
        return "Error processing audio."

if __name__ == "__main__":
    # Test with a sample file
    test_audio = "test_audio.mp3"
    print(transcribe_audio(test_audio))



