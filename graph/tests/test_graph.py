import pytest
from graph import Graph

@pytest.fixture
def single_vertex_edge():
    g = Graph()
    vertex1 = g.add_vertix("X")
    vertex2 = g.add_vertix("Y")
    vertex3 = g.add_vertix("Z")
    vertex4 = g.add_vertix("W")
   
    return g, vertex1, vertex2, vertex3, vertex4

def test_vertex_added_to_graph(single_vertex_edge):
    g, v1, _, _, _ = single_vertex_edge
    vertices = g.get_vertices()
    assert len(vertices) == 4
    assert v1 in vertices

def test_edge_added_to_graph(single_vertex_edge):
    g, v1, v2, v3, v4= single_vertex_edge
    g.add_edge(v1, v2)
    neighbors_v1 = g.get_neighbors(v1)
    assert len(neighbors_v1) == 1
    assert neighbors_v1[0].vertix == v2

def test_retrieve_all_vertices(single_vertex_edge):
    g, v1, v2, v3, v4 = single_vertex_edge
    vertices = g.get_vertices()
    assert len(vertices) == 4
    assert all(v in vertices for v in [v1, v2, v3, v4])

def test_retrieve_appropriate_neighbors(single_vertex_edge):
    g, v1, v2, v3, v4 = single_vertex_edge
    v3 = g.add_vertix("Z")
    g.add_edge(v1, v2)
    g.add_edge(v1, v3)
    
    neighbors_v1 = g.get_neighbors(v1)
    assert len(neighbors_v1) == 2
    assert any(edge.vertix == v2 for edge in neighbors_v1)
    assert any(edge.vertix == v3 for edge in neighbors_v1)

def test_neighbors_returned_with_weight(single_vertex_edge):
    g, v1, v2, v3, v4 = single_vertex_edge
    g.add_edge(v1, v2, weight=3)
    
    neighbors_v1 = g.get_neighbors(v1)
    assert len(neighbors_v1) == 1
    assert neighbors_v1[0].vertix == v2
    assert neighbors_v1[0].weight == 3

def test_proper_size_returned(single_vertex_edge):
    g,v1, v2, v3, v4 = single_vertex_edge
    assert g.size() == 4

def test_graph_with_single_vertex_edge(single_vertex_edge):
    g, v1, v2, v3, v4 = single_vertex_edge
    neighbors_v1 = g.get_neighbors(v1)
    assert len(neighbors_v1) == 0

