import pytest
from depth_first import Graph, Node

@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')
    graph.add_node('H')

    graph.add_edge(graph.nodes[0], graph.nodes[1])  
    graph.add_edge(graph.nodes[0], graph.nodes[2])  
    graph.add_edge(graph.nodes[1], graph.nodes[3])  
    graph.add_edge(graph.nodes[1], graph.nodes[4])  
    graph.add_edge(graph.nodes[2], graph.nodes[6])  
    graph.add_edge(graph.nodes[3], graph.nodes[5])  
    graph.add_edge(graph.nodes[6], graph.nodes[7])  

    return graph

def test_depth_first(sample_graph):
    start_node = sample_graph.nodes[0]
    result = sample_graph.depth_first(start_node)
    assert result == ['A', 'B', 'D', 'F', 'E', 'C', 'G', 'H']

