from collections import defaultdict
import pdb

class Node:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data

    def __repr__(self):
        result = "name: {}".format(self.name)
        if self.data:
            result += ", data: {}".format(self.data)
        return result

    def __eq__(self, node):
        return self.name == node.name

class NodeCollection(dict):
    def _node_exists(self, node):
        return node.name in self

    def add_node(self, node):
        result = False
        if not self._node_exists(node):
            self.update({node.name: node})
            result = True
        return result

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def remove_node(self, node):
        result = False
        if self._node_exists(node):
            self.pop(node.name)
            result = True
        return result

class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.name = "{},{}".format(self.vertex1.name, self.vertex2.name)

    @property
    def name_reversed(self): 
        return "{},{}".format(self.vertex2.name, self.vertex1.name)

    def connection_exists(self, edge):
        result = False
        if edge.vertex1 in self.vertices or\
           edge.vertex2 in self.vertices:
            result = True
        return result

    @property
    def vertices(self):
        return self.vertex1, self.vertex2

    def __repr__(self):
        return "vertexs: ({}, {})".format(self.vertex1.name,
                                          self.vertex2.name)
    def __eq__(self, edge):
        return sorted(edge.name.split(",")) == sorted(self.name.split(","))

# TODO: need to be able to remove relationships and relationships
# associated with relationsips!
class EdgeCollection(defaultdict):
    def __init__(self):
        super().__init__(list)

    def add_relationships(self, edge):
        result = False
        for key, items in self.items():
            if not edge in items:
                if edge.connection_exists(items[0]):
                    self[key].append(edge)
                    result = True
        return result

    def add_all_relationships(self):
        for items in self.values():
            self.add_relationships(items[0])

    def remove_relationships(self, edge):
        result = False
        for key, items in self.items():
            if edge in items:
                items.remove(edge)
                result = True
        return result

    def node_to_edge_list(self, node):
        result = []
        for key, items in self.items():
            if node in items[0].vertices:
                results.append(item[0])
        return items

    def remove_relationships_by_node(node):
        edges = self.node_to_edge_list(node)
        for edge in edges:
            self.remove_relationship(edge)

    def add_edge(self, edge):
        result = False
        if not edge.name in self and\
           not edge.name_reversed in self:
            self[edge.name].append(edge)
            self.add_all_relationships()
            result = True
        return result

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def remove_edge(self, edge):
        result = False
        if edge.name in self:
            del self[edge.name]
            result = True
        return result

    def remove_node(self, node):
        result = []
        for key, items in self.items():
            if node.name in key:
                result.append(items[0])

        for item in result:
            self.remove_edge(item)
        return result

    def remove_self_loops(self):
        # Not sure if this is needed...
        result = []
        for edge_name, edges in self.items():
            if len(edges) > 1:
                while edges[0] in edges[1:]:
                    index = edges[1:].index(edge[0]) + 1
                    edges.pop(index)

# Need to rewrite after creating EdgeCollection and
# NodeCollection classes.
class Graph:
    def __init__(self, nodes=NodeCollection, edges=EdgeCollection):
        self.nodes = nodes()
        self.edges = edges()

    def add_node(self, new_node):
        return self.nodes.add_node(new_node)

    def add_nodes(self, nodes):
        self.nodes.add_nodes(nodes)

    def add_edge(self, new_edge):
        self.nodes.add_nodes(new_edge.itervalues())
        self.edges.add_edge(edge)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)
        
    def remove_edge(self, old_edge):
        return self.edges.remove_edge(old_edge)

    def remove_node(self, old_node):
        value1 = self.nodes.remove_node(old_node)
        value2 = self.edges.remove_node(old_node)
        return value1, value2

    def remove_nodes(self, nodes):
        for node in nodes:
            self.nodes.remove_node(node)
            self.edges.remove_node(node)
