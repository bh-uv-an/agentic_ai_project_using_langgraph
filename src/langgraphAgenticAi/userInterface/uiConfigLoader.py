from configparser import ConfigParser 
# Here configparser will be responsible for loading configurations from ini file 

class Config:
    def __init__(self, config_file=r"C:\Users\Bhuvan Shetty\My Project\Agentic-AI-Langgraph\src\langgraphAgenticAi\userInterface\uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")

    def get_page_title(self):
        return [self.config["DEFAULT"].get("PAGE_TITLE")]

    def get_openai_model_options(self):
        return self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS")

    def get_gemini_models(self):
        return self.config["DEFAULT"].get("GEMINI_MODEL_OPTIONS").split(", ")

    def get_usecase_options(self):
        return [self.config["DEFAULT"].get("USECASE_OPTION")]