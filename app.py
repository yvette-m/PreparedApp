import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os 
import re
import pandas as pd 



        
# Function to load and preprocess the custom text file
def load_text_file(Prepared_data):
    file_path = os.path.join(os.getcwd(), Prepared_data)  # Ensure file is in the same directory
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()] # Return non-empty lines

# Function to load the merged CSV file
def load_csv(amazon_link):
    """
    Load the unified CSV file into a pandas DataFrame.
    """
    return pd.read_csv(amazon_link)

# Extract ZIP code or address from the user query
def extract_location_details(query):
    """
    Extract ZIP code or address from the user query.
    """
    zip_code_match = re.search(r"\b\d{5}\b", query)  # Match 5-digit ZIP codes
    address_match = re.search(r"at (.+?)(,|\.|$)", query, re.IGNORECASE)  # Match address after 'at'
    return zip_code_match.group() if zip_code_match else None, address_match.group(1).strip() if address_match else None

# Find hazards for a ZIP code or location
def find_hazards(data, zip_code=None, address=None):
    """
    Find hazards in the dataset for a given ZIP code or address.
    """
    if zip_code:
        for line in data:
            if zip_code in line and "hazard" in line.lower():
                return line
    if address:
        for line in data:
            if address.lower() in line.lower() and "hazard" in line.lower():
                return line
    return None

# Find FEMA guidelines based on a hazard
def find_fema_guidelines(data, hazard):
    """
    Find FEMA preparedness guidelines for a specific hazard.
    """
    for line in data:
        if hazard.lower() in line.lower() and "FEMA" in line:
            return line
    return None

# Search for recommendations in the merged CSV
def search_recommendations(data, query):
    """
    Search the merged CSV for matches to the query.
    """
    query = query.lower()
    results = data[
        data['Notes/Information'].str.lower().str.contains(query, na=False) |
        data['Items to be purchased or self supplied'].str.lower().str.contains(query, na=False)
    ]
    return results

# Query classification function
def classify_query(query):
    greetings = ["hi", "hello", "how are you", "good morning", "good evening"]
    jokes = ["tell me a joke", "make me laugh"]
    preparedness_keywords = ["prepared", "hazard", "risk", "emergency", "earthquake", "flood"]

    query_lower = query.lower()
    if any(greet in query_lower for greet in greetings):
        return "greeting"
    elif any(joke in query_lower for joke in jokes):
        return "joke"
    elif any(keyword in query_lower for keyword in preparedness_keywords):
        return "preparedness"
    else:
        return "general"



# Load custom data
custom_data = load_text_file("Prepared_data.txt")
amazon_data = load_csv("amazon_link.csv")       # Unified product recommendation data


# Set up the chatbot template and model
template = """
You are an advanced preparedness chatbot. Use the information below to provide specific and personalized responses.

Preparedness Data: {preparedness_data}

Amazon Recommendations: {amazon_data}

Here is the conversation history: {context}

Question: {question}


Answer:
1. Introduction: Provide guidance on how the user and their family can prepare for the specific hazard or emergency.
2. Things to Get: List essential items needed for the hazard or emergency, including detailed descriptions.
3. Amazon Recommendations: Provide a list of recommended items with links to purchase.

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit app setup
st.title("Preparedness Chatbot")



# Initialize session state to keep conversation history
if "context" not in st.session_state:
    st.session_state["context"] = []



# Input form for user prompt
user_query = st.text_input("Ask about your area's preparedness or risks:")

if st.button("Submit"):
    st.write("Processing your query...")

    # Step 1: Classify the user query
    query_type = classify_query(user_query)

    if query_type == "greeting":
        response = "Hi! I'm good, thank you! How can I assist you today?"
        st.session_state["context"].append(f"AI: {response}")
        st.write(response)

    elif query_type == "joke":
        response = "Why don’t skeletons fight each other? They don’t have the guts!"
        st.session_state["context"].append(f"AI: {response}")
        st.write(response)

    elif query_type == "preparedness":
        # Step 2: Extract location details
        zip_code, address = extract_location_details(user_query)

        # Step 3: Check for hazards
        hazard_info = find_hazards(custom_data, zip_code, address)

        preparedness_data = ""
        amazon_recommendations = ""

        if hazard_info:
            preparedness_data += f"- Hazard Information: {hazard_info}\n"

            # Find relevant FEMA guidelines
            hazard_type = "earthquake" if "earthquake" in hazard_info.lower() else "flood" if "flood" in hazard_info.lower() else "hazard"
            fema_guidelines = find_fema_guidelines(custom_data, hazard_type)
            if fema_guidelines:
                preparedness_data += f"- FEMA Guidelines: {fema_guidelines}\n"

            # Search for recommendations
            recommendations = search_recommendations(amazon_data, hazard_type)
            if not recommendations.empty:
                for _, row in recommendations.iterrows():
                    amazon_recommendations += f"- **Item**: {row['Items to be purchased or self supplied']} | **Details**: {row['Notes/Information']} | **Buy Here**: {row['Amazon Item (placeholder)']}\n"

        # Invoke Llama 3 model
        result = chain.invoke({
            "preparedness_data": preparedness_data,
            "amazon_data": amazon_recommendations,
            "context": st.session_state["context"],
            "question": user_query
        })

        # Append chatbot response to history
        st.session_state["context"].append(f"AI: {result}")
        st.write("### Here’s how you and your family should be prepared:")
        st.write(result)

        # Add Amazon recommendations
        if amazon_recommendations:
            st.write("### Amazon Recommendations:")
            for line in amazon_recommendations.split("\n"):
                if line.strip():
                    st.write(line)

    else:
        response = "I'm here to assist with preparedness-related questions. Can you clarify your request?"
        st.session_state["context"].append(f"AI: {response}")
        st.write(response)

    # Append user query to context
    st.session_state["context"].append(f"User: {user_query}")
