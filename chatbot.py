from openai import OpenAI
import streamlit as st

# Streamlit app title and sidebar for OpenAI API key input
st.title("🤖 Chatbot")
st.caption("🚀 A Streamlit chatbot by Hema")

# Input field for OpenAI API key in the sidebar
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

# Initialize or retrieve existing messages from session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display existing chat messages
for msg in st.session_state.messages:
    st.text(f"{msg['role']}: {msg['content']}")

# Chat input field for user interaction
if prompt := st.text_input("You", key="user_input"):
    if not openai_api_key:
        st.warning("Please add your OpenAI key to continue.")
        st.stop()

    # Initialize OpenAI client with provided API key
    client = OpenAI(api_key=openai_api_key)

    # Add user input to session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Chat message display for user input
    st.text(f"user: {prompt}")

    # Generate response using OpenAI's GPT-3.5 model
    response = client.ChatCompletion.create( model="gpt-3.5-turbo",messages=st.session_state.messages  )

    # Extract and display assistant's response
    msg = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.text(f"assistant: {msg}")
