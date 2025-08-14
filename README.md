# Voice2Vision

**Voice2Vision** is a Streamlit web application that transforms your voice into a visual summary and downloadable PDF using OpenAI's Whisper, GPT, and DALL·E APIs.

## Features

- **Audio Input:** Upload or record your voice directly in the browser.
- **Transcription:** Transcribe audio online using OpenAI Whisper.
- **Summarization:** Summarize the transcript with GPT.
- **Image Generation:** Generate a unique image from the summary using DALL·E.
- **PDF Export:** Download a PDF containing the summary and generated image.


## Setup

**Add your API keys:**
   - Create a `.env` file in the project root.
   - Add your OpenAI and Hugging Face API keys:
     ```
     OPENAI_API_KEY=your_openai_key
     HUGGINGFACE_TOKEN=your_huggingface_token
     ```

