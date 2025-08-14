import os
import streamlit as st
from dotenv import load_dotenv
from utils.audio_recorder import get_audio_input
from utils.transcriber import transcribe_audio
from utils.summarizer import summarize_text
from utils.image_generator import generate_image_from_text
from utils.pdf_generator import generate_pdf

# Load environment variables
print(load_dotenv(dotenv_path=".env"))

# Set Streamlit page config
st.set_page_config(page_title="Voice2Vision", layout="centered")

# Initialize session state
for key in ["audio_file", "transcript", "summary", "image_path", "pdf_path"]:
    if key not in st.session_state:
        st.session_state[key] = None

# Title
st.title("Voice2Vision")
st.markdown("Turn your **voice** into a **visual summary** and downloadable **PDF** using OpenAI's Whisper, GPT, and DALL·E.")

# Step 1: Audio Input
st.header("1. Upload or Record Your Audio")
audio_file = get_audio_input()
print("Audio file path is :", audio_file)
if audio_file:
    st.session_state.audio_file = audio_file
    st.success("Audio ready! Proceed to transcription.")

# Step 2: Transcription
if st.session_state.audio_file:
    st.header("2. Transcribe Audio")
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing with Whisper..."):
            st.session_state.transcript = transcribe_audio(st.session_state.audio_file)
            #Remove the audio file after transcription
            if os.path.exists(st.session_state.audio_file):
                os.remove(st.session_state.audio_file)

    if st.session_state.transcript:
        st.text_area("Transcript", value=st.session_state.transcript, height=200)

# Step 3: Summarization
if st.session_state.transcript:
    st.header("3. Summarize the Transcript")
    if st.button("Summarize Transcript"):
        with st.spinner("Summarizing with GPT..."):
            st.session_state.summary = summarize_text(st.session_state.transcript)

    if st.session_state.summary:
        st.text_area("Summary", value=st.session_state.summary, height=200)

# Step 4: Image Generation
if st.session_state.summary:
    st.header("4. Generate Image from Summary")
    if st.button("Generate Image"):
        print("Generating image from summary...")
        with st.spinner("Generating image with DALL·E..."):
            print("image generation")
            st.session_state.image_path = generate_image_from_text(st.session_state.summary)
            print("Image generated at:", st.session_state.image_path)
            print("image generation Done")
    if st.session_state.image_path and os.path.exists(st.session_state.image_path):
        st.image(st.session_state.image_path, caption="Generated from summary", use_column_width=True)

# Step 5: PDF Export
if st.session_state.summary and st.session_state.image_path:
    st.header("5. Export Summary + Image as PDF")
    if st.button("Generate PDF"):
        with st.spinner("Creating PDF..."):
            st.session_state.pdf_path = generate_pdf(
                st.session_state.summary,
                st.session_state.image_path
            )
            st.success("PDF ready!")
            with open(st.session_state.pdf_path, "rb") as f:
                st.download_button("📄 Download PDF", f, file_name="voice2vision_summary.pdf")
