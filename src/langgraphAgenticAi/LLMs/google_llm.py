import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

class GoogleLLM:
    def __init__(self, user_conf=None):
        if user_conf is None:
            st.error("User Configuration required to initiate model!")
    
        self.user_conf = user_conf

    def get_llm_model(self):
        try:
            model = self.user_conf['selected_model']
            api_key = self.user_conf['selected_model_api_key']
        
            llm_model = ChatGoogleGenerativeAI(model=model, api_key=api_key)
            return llm_model
        
        except Exception as err:
            st.error(f"Unable to connect with OpenAI Error:{err}")
            return None