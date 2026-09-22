import streamlit as st
from langchain_core.messages import HumanMessage

class DisplayStreamlitResult:
    def __init__(self, graph, user_query):
        self.graph = graph
        self.user_query = user_query
 
    def display_result(self):
        with st.chat_message("user"):
            st.write(self.user_query)
        with st.chat_message("ai"):
            graph_result = self.graph.invoke({
                'messages' : [HumanMessage(content=self.user_query)]
            })
            print(graph_result)
            st.write(graph_result['messages'][-1].content)