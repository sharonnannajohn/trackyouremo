import streamlit as st
import time
import emo

# Streamed response emulator
def response_generator(prompt):
    response = emo.GenerateResponse(prompt)  # Call the chatbot function
    
    for word in response.split():
        yield word + " "  # Simulate a streaming response
        time.sleep(0.05)

st.title("Eirene - AI Healthcare Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    response = ""
    with st.chat_message("assistant"):
        for word in response_generator(prompt):
            response += word
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})