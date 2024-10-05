import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu
from gemini_utility import (load_gemini,load_image,embedding_model)
working_directory = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title="Pradyumna too sigma escape matrix",
    page_icon="☠️",
    layout="centered"
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["Chatbot",
                           "Image",
                            "Embed text"],
                           menu_icon= 'robot', icons=['chat-fill','image','textarea-t','question-circle-fill'],
                           default_index=0)

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if selected == "Chatbot":
    model = load_gemini()
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
    st.title("Chatbot🤖")

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_promt = st.chat_input("Ask THE bot....")

    if user_promt:
        st.chat_message("user").markdown(user_promt)

        response = st.session_state.chat_session.send_message(user_promt)

        with st.chat_message("assistant"):
            st.markdown(response.text)

if selected == "Image":
    st.title("Snap Narrate")
    uploaded_image = st.file_uploader("Upload an image....", type=["jpg, jpeg","png"])
    if st.button("Genearate Caption"):
        image = Image.open(uploaded_image)
        col1,col2=st.columns(2)

        with col1:
            resized_image = image.resize((800,500))
            st.image(resized_image)

        default_prompt = "write a short caption for this image"

        caption = load_image(default_prompt,image)
        with col2:
            st.info(caption)

if selected == "Embed text":
    st.title("Embed text")
    input_text = st.text_area(label="", placeholder="Enter the text to get the embeddings")

    if st.button("get Embeddings"):
        response = embedding_model(input_text)
        st.markdown(response)
