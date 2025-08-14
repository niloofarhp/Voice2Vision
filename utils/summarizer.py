import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(transcript: str, model="gpt-4") -> str:
    """
    Summarizes the given transcript using GPT model.
    """
    try:
        system_prompt = (
            "You are an assistant that summarizes voice transcripts into clear and concise paragraphs. "
            "Summarize the content in a professional tone."
        )
        user_prompt = f"Here is the transcript:\n\n{transcript}\n\nPlease provide a summary:"

        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.5,
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        return f"[ERROR] Failed to summarize: {str(e)}"
