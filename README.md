# ChatGPT with ApnaGPT

# Overview
This application demonstrates the integration of ChatGPT (based on OpenAI's GPT model) with ApnaGPT, a custom chatbot built using Azure OpenAI. Users can interact with the chatbot by typing messages, and the chatbot will respond with generated text based on the conversation history.

# Requirements
- Python 3.x
- Streamlit
- Langchain_openai
- dotenv
- Azure OpenAI API key
- Azure OpenAI endpoint

# Installation
* Clone the repository:
```
git clone https://github.com/your-repo.git
cd your-repo
```
* Install dependencies:
```
pip install -r requirements.txt
```
* Set up environment variables:
* Create a .env file in the project root directory and add the following:
```
API_KEY=your_openai_api_key
ENDPOINT=your_azure_openai_endpoint
API_VERSION=your_azure_openai_api_version
MODEL_NAME=your_azure_openai_model_name
```

# Usage
Run the application by executing:
```
streamlit run app.py
```

Upon launching the application, it will check for the presence of required environment variables and set up Streamlit page configurations.
- Users can interact with the chatbot by typing messages in the chat input field.
- The chatbot responds with generated text based on the conversation history.
- The message history is displayed on the screen, alternating between user and AI messages.

# Functionality
1. Initialization: The application initializes the chatbot with the Azure OpenAI endpoint, API key, API version, and model name provided in the environment variables.
2. User Interaction: Users can type messages into the chat input field, simulating a conversation with the chatbot.
3. Message History: The application keeps track of the conversation history, displaying user and AI messages in a chronological order.
4. Error Handling: The application checks for the presence of required environment variables and exits with an error message if any of them are missing.

# License
This project is licensed under the MIT License.
