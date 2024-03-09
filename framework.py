import streamlit as st
import requests
from bs4 import BeautifulSoup


# Initialize Streamlit app
st.title("BhilaiGPT - Query System for IIT Bhilai")


# Function to scrape documents from IIT Bhilai website
def scrape_documents():
    # URL of IIT Bhilai website
    url = "https://www.iitbhilai.ac.in/"


    # Send request to the website with SSL certificate verification disabled
    response = requests.get(url, verify=False)


    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")


    # Extract relevant document links
    document_links = []
    for link in soup.find_all("a"):
        if "student handbook" in link.text.lower() or "academic calendar" in link.text.lower():
            document_links.append(link.get("href"))


    return document_links
# Function to process user query
def process_query(query):
    # Implement your custom NLP model here
    # For demonstration purposes, let's just return a dummy response
   
    response = "This is a dummy response. Replace it with your actual NLP model output."
    return response


# Container for user input
user_query = st.text_input("Enter your query:")


# Button to submit query
if st.button("Submit"):
    # Process user query
    if user_query:
        response = process_query(user_query)
        st.write("Response:")
        st.write(response)
    else:
        st.error("Please enter a query.")


# Bonus Feature: Display document links
document_links = scrape_documents()
if document_links:
    st.write("Related Documents:")
    for link in document_links:
        st.write(link)
else:
    st.write("No relevant documents found.")


# Bonus Feature: History
def save_query_history(query):
    # Implement logic to save query history
    pass


# Bonus Feature: Feedback option
def get_feedback():
    feedback = st.text_input("Provide feedback to improve the model:")
    if st.button("Submit Feedback"):
        # Implement logic to collect and process feedback
        st.success("Thank you for your feedback!")


# Save query history
if user_query:
    save_query_history(user_query)


# Display feedback option
get_feedback()



