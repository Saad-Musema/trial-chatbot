import streamlit as st
from gemini_ai import GeminiAI

# Initialize the AI (Replace 'YOUR_API_KEY' with your actual API key)
gemini = GeminiAI(api_key="AIzaSyASnkyIRB2Abu4qUY8yfI8K_2sYLqhh5io")

# Streamlit app title
st.title("GeminiAI Interface")

# Sidebar configuration
st.sidebar.header("Model Configuration")
temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.9)
gemini.config(temp=temp, top_p=top_p)

# Input for chat instruction
instruction = st.text_input("Enter a chat instruction", "Tell me about recent advancements in AI")
if st.button("Start Chat Session"):
    gemini.start_chat(instruction=instruction)
    st.success("Chat session started with instruction: " + instruction)

# Input for sending a prompt
prompt = st.text_input("Enter a message to send to GeminiAI")
if st.button("Send Message"):
    response = gemini.send_message(prompt)
    st.text_area("GeminiAI Response", value=response, height=200)

# Button to view chat history
if st.button("View Chat History"):
    history = gemini.history()
    st.text_area("Chat History", value=history, height=200)