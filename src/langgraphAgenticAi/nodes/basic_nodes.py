from src.langgraphAgenticAi.state.state import State

class basic_chatbot_node:
    def __init__(self, llm):
        self.llm = llm 

    def load_basic_node_implemenation(self, state: State):
        return {"messages": self.llm.invoke(state["messages"])}