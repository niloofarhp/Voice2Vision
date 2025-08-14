import streamlit as st
import os
import tempfile
from audio_recorder_streamlit import audio_recorder
def get_audio_input():
    st.header("🎤 Audio Input")
    
    option = st.radio("Choose input method:", ["Record Audio", "Upload File"])

    audio_bytes = None
    file_path = None

    if option == "Record Audio":
        audio_bytes = audio_bytes = audio_recorder(
                                        text="",
                                        recording_color="#e8b62c",
                                        neutral_color="#6aa36f",
                                        icon_name="user",
                                        icon_size="6x",
                                    )#audio_recorder(label="Record something...", format="audio/wav")
        if audio_bytes:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav", dir="audio") as f:
                f.write(audio_bytes)
                file_path = f.name
    else:
        uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])
        print("uploading the file is :", uploaded_file)
        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name, dir="audio") as f:
                f.write(uploaded_file.read())
                file_path = f.name
                print("File Path : ", file_path)
                f.close()

    return file_path
