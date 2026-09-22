from src.langgraphAgenticAi.state.state import State
from src.langgraphAgenticAi.nodes.basic_nodes import basic_chatbot_node
from langgraph.graph import StateGraph, START, END


class GraphBuilder:
    def __init__(self, llm_model):
        self.graph_builder = StateGraph(State)
        self.llm_model = llm_model

    def basic_chatbot_build_graph(self):
        chatbot_node = basic_chatbot_node(self.llm_model)

        self.graph_builder.add_node("basic_chatbot", chatbot_node.load_basic_node_implemenation)
        self.graph_builder.add_edge(START, "basic_chatbot")
        self.graph_builder.add_edge("basic_chatbot", END)

        final_graph = self.graph_builder.compile()
        return final_graph