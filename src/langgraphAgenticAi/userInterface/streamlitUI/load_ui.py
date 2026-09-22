import streamlit as st  # type: ignore[import-not-found]
import os 
from dotenv import load_dotenv
from src.langgraphAgenticAi.userInterface.uiConfigLoader import Config

load_dotenv()
"""
    st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, 
    autocomplete=None, on_change="rerun", args=None, kwargs=None, *, placeholder=None, 
    disabled=False, label_visibility="visible", icon=None, validate=None, live=False, 
    width="stretch", bind=None, persist_state=None                

    st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, 
    help=None, on_change="rerun", args=None, kwargs=None, *, placeholder=None, 
    disabled=False, label_visibility="visible", accept_new_options=False, 
    filter_mode="fuzzy", width="stretch", bind=None, persist_state=None)

    st.chat_input(placeholder="Your message", *, key=None, max_chars=None, max_upload_size=None, accept_file=False, file_type=None, 
    accept_audio=False, audio_sample_rate=16000, disabled=False, submit_mode="submit", on_submit=None, args=None, kwargs=None, 
    width="stretch", height="content")
"""


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=f"{self.config.get_page_title()[0]}", layout="wide")
        st.header(f"{self.config.get_page_title()[0]}")

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox(label="Select Your LLM", options=llm_options)
            selected_llm = self.user_controls["selected_llm"]

            if selected_llm == "OpenAI":
                model_options = self.config.get_openai_model_options() 
                self.user_controls["selected_model_api_key"] = os.getenv("COMPANY_OPENAI_API_KEY")
            elif selected_llm == "Gemini":
                model_options = self.config.get_gemini_models()
                self.user_controls["selected_model_api_key"] = os.getenv("GEMINI_API_KEY")

            self.user_controls["selected_model"] = st.selectbox(label="Select OpenAI Models", options=model_options)

            
            self.user_controls["selected_use_case"] = st.selectbox(label="Selected Use-Case", options=usecase_options)

        return self.user_controls

    def get_user_query(self):
        try:
            user_prompt = st.chat_input(placeholder="Enter your message")
            return user_prompt
        except Exception as err:
            print(f"Unable to get the user Query from the User!: {err}")
            return None


                           
