import os
import google.generativeai as ai
import json

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

KEY = config_data["KEY"]

ai.configure(api_key=KEY)

def load_gemini():
    gemini_model = ai.GenerativeModel("gemini-pro")
    return gemini_model

def load_image(prompt, image):
    gemini_image = ai.GenerativeModel("gemini-1.5-flash")
    response_cv = gemini_image.generate_content([prompt,image])
    result = response_cv.text
    return result

def embedding_model(input_text):
    embedding_model = "models/embedding-001"
    embedding = ai.embed_content(model=embedding_model,content=input_text,task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list