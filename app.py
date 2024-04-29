import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message

from langchain_openai import AzureChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def gpt():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # test that the API key exists
    if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # setup streamlit page
    st.set_page_config(
        page_title="ChatGPT with ApnaGPT",
        page_icon="🤖"
    )

    # chat = ChatOpenAI(temperature=0)
    client = AzureChatOpenAI(
        azure_endpoint=os.getenv("ENDPOINT"),
        api_key=os.getenv("API_KEY"),
        api_version=os.getenv("API_VERSION"),
        model=os.getenv("MODEL_NAME"),
    )
    
    # initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    st.header("Your own ChatGPT 🤖")

    # sidebar with user input
    prompt = st.chat_input("Say something")

    # handle user input
    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.spinner("Thinking..."):
            response = client(st.session_state.messages)
        st.session_state.messages.append(
            AIMessage(content=response.content))

    # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == '__main__':
    gpt()