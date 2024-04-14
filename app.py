import streamlit as st 
import pydub 
import google.generativeai as genai 
from dotenv import load_dotenv 
import tempfile 

genai.configure(api_key="AIzaSyCfX4WWP-THMPKeGutwdeCkkhstyWTr2kk")


def summarize_Audio(audio_file_path):
    model = genai.GenerativeModel("model/gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    response = model.generative_content(
        [
            "Please summarize the following audio",
            audio_file
        ]
    )
    return response.text 

def save_upload_file(upload_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(upload_file.read())
            return temp.name
    except Exception as e:
        print(e)

#streamlit 
st.title("Audio Summarization")

with st.expander("About the app"):
    st.write("This app summarizes audio files using the Gemini AI model")
    st.write("Made by Dhanushkumar")

    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])
    if audio_file:
        st.audio(Audio_file, format="audio/wav")
        if st.button("Summarize"):
            file_path = save_upload_file(audio_file)
            summary = summarize_Audio(file_path)
            st.write(summary)
