import streamlit as st
import google.generativeai as genai

# Configure the API (Replace 'YOUR_API_KEY' with your actual API key)
genai.configure(api_key="AIzaSyASnkyIRB2Abu4qUY8yfI8K_2sYLqhh5io")

# Streamlit app title
st.title("Google Generative AI Interface")

# Sidebar configuration
st.sidebar.header("Model Selection")
model_name = st.sidebar.selectbox("Choose a model", ["gemini-1.5-flash", "gemini-1.0", "other-model"])

# Initialize the model
model = genai.GenerativeModel(model_name)

# Input for user prompt
prompt = st.text_input("Enter a prompt", "Explain how AI works")
if st.button("Generate Response"):
    try:
        response = model.generate_content(prompt)
        st.text_area("AI Response", value=response.text, height=200)
    except Exception as e:
        st.error(f"An error occurred: {e}")
