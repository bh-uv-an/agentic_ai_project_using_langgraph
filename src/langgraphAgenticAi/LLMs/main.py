from src.langgraphAgenticAi.LLMs.google_llm import GoogleLLM
from src.langgraphAgenticAi.LLMs.openai_llm import OpenAILLM
import streamlit as st

class LoadLLM:
    def __init__(self, user_conf):
        self.user_conf = user_conf
        self.choosen_llm = user_conf['selected_llm']

    def load_llm_model(self):
        if self.choosen_llm == "Gemini":
            google_service = GoogleLLM(user_conf=self.user_conf)
            return google_service.get_llm_model()

        elif self.choosen_llm == "OpenAI":
            openai_service = OpenAILLM(user_conf=self.user_conf)
            return openai_service.get_llm_model()

        else:
            st.error("!Uknown LLM type")
            return None
        
        