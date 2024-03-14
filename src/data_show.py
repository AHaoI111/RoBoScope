from src.Data import Graph


def get_DataFile_ID():
    Graph_ = Graph.Graph()
    node_list = Graph_.RootNode()
    return node_list, Graph_
