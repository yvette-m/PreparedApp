from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os

# Set the remote Ollama host
os.environ["OLLAMA_HOST"] = "https://d664-34-125-46-118.ngrok-free.app/"

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Use the remote Ollama model
model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

st.title("Ask Bot")

# Initialize session state for conversation context and message history
if "context" not in st.session_state:
    st.session_state["context"] = ""

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display the chat history
for message in st.session_state["messages"]:
    st.write(message)

# Callback to process input and clear text box
def handle_input():
    user_input = st.session_state["user_input"]  # Retrieve input
    if user_input:
        try:
            # Generate response using the remote Ollama model
            result = chain.invoke({"context": st.session_state["context"], "question": user_input})

            # Append the conversation to the message history
            st.session_state["messages"].append(f"**User:** {user_input}")
            st.session_state["messages"].append(f"**Bot:** {result}")

            # Update conversation context
            st.session_state["context"] += f"\nUser: {user_input}\nAI: {result}"

        except Exception as e:
            st.error(f"An error occurred: {e}")

        # Clear the input field
        st.session_state["user_input"] = ""

# Input box with on_change callback
st.text_input(
    "Pass Your Prompt here",
    key="user_input",
    on_change=handle_input,  # Process input on text submission
)
