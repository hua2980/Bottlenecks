"""
    CS5001 Fall 2022
    Assignment number of info
    Name / Partner
"""

from graph import *


def create_random_graph(num_vert: int, num_edge: int):
    """
    Create a random graph with the defined number of edges and vertices.
    :param num_vert:
    :param num_edge:
    :return:
    """
    graph = EdgeWeightDigraph()

    # add vertices
    for i in range(num_vert):
        graph.add_vertex(i)

    # add edges
    i = 0
    visited = {}
    while i < num_edge:
        from_v = randint(0, num_vert-1)
        to_v = randint(0, num_vert - 1)

        if from_v not in visited:
            visited[from_v] = set()
        while to_v in visited[from_v]:
            to_v = randint(0, num_vert - 1)

        if from_v == to_v:
            continue

        visited[from_v].add(to_v)
        graph.add_edge(from_v, to_v)
        i += 1
    return graph


def main():
    # create a random graph
    graph = create_random_graph(5, 10)  # 5 is the number of vertex. 10 is the number of edge

    # access adjacency dictionary
    adj_list_output = graph.get_output_vert_dict()
    print(adj_list_output)
    adj_list_input = graph.get_input_vert_dict()
    print(adj_list_input)

    # get edges
    edge = graph.get_edgeTo(1, adj_list_output[1][0])

    # get the length of that edge
    length = edge.length

    # get all the edges going out of 1, 2, ...
    for i in range(graph.num_vertices):
        for v in adj_list_output[i]:
            print(graph.get_edgeTo(i, v))

    # get all the edges going in to 1, 2, ...
    for i in range(graph.num_vertices):
        for v in adj_list_input[i]:
            print(graph.get_edgeTo(v, i))

    # get all vertices in the graph
    vertex_list = graph.get_vertices()


if __name__ == '__main__':
    main()
