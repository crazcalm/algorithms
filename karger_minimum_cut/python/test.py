import networkx
import random

edges = [(1,2), (1,4), (2,1), (2,3), (2,4), (4,1), (4,2), (4,3)]

test = networkx.Graph()
test.add_edges_from(edges)
print("nodes: {}".format(test.nodes(data=True)))
print("edges: {}".format(test.edges()))

print("an edge: {}".format(test.edges()[0]))
print("1 in edge: {}".format(1 in test.edges()[0]))

"""
Karger's cut steps:

1)  Initialize contracted graph CG as copy of original graph
2)  While there are more than 2 vertices.
      a) Pick a random edge (u, v) in the contracted graph.
      b) Merge (or contract) u and v into a single vertex (update 
         the contracted graph).
      c) Remove self-loops
3) Return cut represented by two vertices.
"""

def karger_min_cut(graph):
    test = graph.edges()
    num_of_nodes = len(graph)
    while num_of_nodes > 2:  # Number of node greater than 2
        random_edge = graph.edges()[random.randint(0, len(graph.edges()) -1)]
        print("random edge: {}".format(random_edge))
        # merging edges?
        list_of_edges_to_merge = [edge for edge in graph.edges()
                                  if random_edge[0] in edge]

        new_edges = []
        for v1, v2 in list_of_edges_to_merge:
            print("v1: {}, v2: {}".format(v1, v2))
            if v1 == random_edge[0] and v2 != random_edge[1]:
                new_edges.append((random_edge[0], v2))

                # testing this out
                try:
                    test.remove((v1, v2))
                except:
                    pass
                test.append((random_edge[1], v2))
            if v2 == random_edge[0] and v1 != random_edge[1]:
                new_edges.append((v1, random_edge[1]))

                # testing this out
                try:
                    test.remove((v1, v2))
                except:
                    pass
                test.append((v1, random_edge[1]))

            if v1 == random_edge[0] and v2 == random_edge[1]:
                # testing this out
                try:
                    test.remove((v1, v2))
                except:
                    pass
        # remove old edges and add new edges
        graph.remove_node(random_edge[0])
        graph.add_edges_from(new_edges)
        print("new graph: {}".format(graph.edges()))
        print("test: {}".format(test))
        # num of nodes
        num_of_nodes = len(graph)
        print("num of nodes: {}".format(num_of_nodes))
        input("Next:\n")
    return graph.edges()[0]

print(karger_min_cut(test))
