import streamlit as st
from PIL import Image

# List of image file paths
images = [
    '1.png',  # Replace with your image paths
    '2.png',
    '3.png',
    '4.png',
    '5.png'
]

st.title("Basketball Club Management System")

for img_path in images:
    img = Image.open(img_path)
    st.image(img, caption=img_path, use_column_width=True)