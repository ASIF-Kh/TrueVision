import streamlit as st
from utils.image_utils import load_image
from model.image_classifier import load_ai_model, predict_image
from PIL import Image

# Load the AI model
model = load_ai_model()

# Set page configuration
st.set_page_config(
    page_title="TrueVision - Image Authenticity Checker", 
    page_icon="🖼️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Dark theme CSS
st.markdown(
    """
    <style>
    body {
        color: #e0e0e0;
        background-color: #121212;
    }
    .main {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 200px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stFileUploader {
        background-color: #333333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    .stImage {
        border: 1px solid #333333;
    }
    .stSidebar {
        background-color: #333333;
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar content
with st.sidebar:
    st.image("assets/logo.png", width=200)
    st.title("TrueVision")
    st.markdown("**AI-powered Image Authenticity Checker**")
    st.markdown("Upload an image and let our AI determine if it's real or manipulated.")

# Main title and description
st.title("🔍 Check Your Image's Authenticity")
st.write("Use our advanced AI model to detect if an image is real or fake. Simply upload an image, and we'll analyze it for you.")

# Layout with two columns
col1, col2 = st.columns([1, 1])

# Column for image upload
with col1:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    else:
        st.info("Please upload an image to begin analysis.")

# Column for prediction results
with col2:
    st.header("Prediction Results")
    if uploaded_file is not None:
        if st.button("Check Image Authenticity"):
            with st.spinner("Analyzing the image..."):
                prediction = predict_image(model, image)
                if prediction == "Real":
                    st.success(f"The image is **{prediction}** 🎉")
                else:
                    st.error(f"The image is **{prediction}** ⚠️")
    else:
        st.warning("Upload an image to enable the prediction.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
    Made with ❤️ by the TrueVision.
    </div>
    """, unsafe_allow_html=True
)
