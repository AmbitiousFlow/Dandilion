import streamlit as st

st.title("Dandilion")
st.markdown("**Cross-platform open-source desktop application that converts YouTube links into various media formats, including audio and video.**")

st.text_input("Enter YouTube link", key="youtube_link")
st.selectbox("Select output format", options=["MP3", "MP4"], key="output_format")
st.button("Download", key="download_button")