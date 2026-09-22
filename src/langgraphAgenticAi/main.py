import streamlit as st

from src.langgraphAgenticAi.userInterface.streamlitUI.load_ui import LoadStreamlitUI
from src.langgraphAgenticAi.userInterface.streamlitUI.display_result import DisplayStreamlitResult
from src.langgraphAgenticAi.LLMs.main import LoadLLM
from src.langgraphAgenticAi.langGraph.graph_builder import GraphBuilder

ui = LoadStreamlitUI()

def load_the_complete_langgraph_application():
    user_conf = ui.load_streamlit_ui()

    if not user_conf:
        st.error("Failed: To load human configuration")
        return
    
    user_query = ui.get_user_query()
    print(user_query)

    if user_query:
        model_loader = LoadLLM(user_conf)
        llm_model = model_loader.load_llm_model()

        graph = GraphBuilder(llm_model)
        final_graph = graph.basic_chatbot_build_graph()

        display_obj = DisplayStreamlitResult(final_graph, user_query)
        result = display_obj.display_result()
        if result is False:
            st.error("!Something went wrong while generating query")
