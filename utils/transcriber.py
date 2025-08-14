import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(audio_file_path: str) -> str:
    try:
        with open(audio_file_path, "rb") as audio_file:
            print(f"Transcribing audio file: {audio_file_path}")
            transcript = openai.audio.transcriptions.create(model="whisper-1", 
                                                            file=audio_file, response_format="text")
            print(f"Transcription : {transcript}")
        return transcript.strip()
    except Exception as e:
        return f"[ERROR] Failed to transcribe: {str(e)}"
