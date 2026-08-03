import streamlit as st
from PIL import Image
from transformers import pipeline  # to run-> streamlit run app.py
import torch

st.set_page_config(page_title="Emotion Detection")
st.title("Facial Emotion Detection Model Using Hugging Face")

def load_model():
    return pipeline("image-classification", 
                    model="trpakov/vit-face-expression"
                    )

classifier = load_model()

upload_file=st.file_uploader(
    "Upload a face image",
    type=["jpg","jpeg","png"]
)

if upload_file:
    image=Image.open(upload_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    with st.spinner("Dectecting Emotion"):
        prediction = classifier(image)

    st.subheader("Predictions")

    for pred in prediction[:5]:
        st.write(
            f"**{pred['label']}**: {pred['score']*100 :.2f}%"
        )

    best = prediction[0]

    st.success(
        f"Detected Emotion:{best['label']} ({best['score']*100 :.2f}%)"
    )