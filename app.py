import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np


# Load the saved model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("potato_model.keras")


with st.spinner("Loading Model..."):
    model = load_model()

# Match these to your dataset's actual class names
class_names = ["Early Blight", "Late Blight", "Healthy"]

st.title("🌱 Potato Disease Classification")
st.write("Upload a potato leaf image to predict whether it is healthy or diseased.")

uploaded_file = st.file_uploader("Choose a potato leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf', use_container_width=True)

    # Preprocess the image to match your model's training size (adjust 256 if your model uses a different size)
    image = image.resize((256, 256))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, 0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)

    st.success(f"**Prediction:** {predicted_class}")
    st.info(f"**Confidence:** {confidence}%")