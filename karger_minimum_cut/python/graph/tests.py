import unittest

from classes import Node, NodeCollection
from classes import Edge, EdgeCollection
from classes import Graph

class TestNode(unittest.TestCase):
    def setUp(self):
        self.data = [1,2,3]
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node1", self.data)

    def tearDown(self):
        pass

    def test__init__(self):
        name = "test"
        node = Node(name)
        self.assertEqual(node.name, name)

        node2 = Node(name, self.data)
        self.assertEqual(node2.data, self.data)

    def test__eq__(self):
        self.assertEqual(self.node1, self.node3)
        self.assertNotEqual(self.node1, self.node2)


class TestNodeCollection(unittest.TestCase):
    def setUp(self):
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node1")
        self.nodes = [self.node1, self.node2, self.node2]
        self.node_collection = NodeCollection()

    def tearDown(self):
        pass

    def test_add_node(self):
        self.assertTrue(self.node_collection.add_node(self.node1))
        self.assertFalse(self.node_collection.add_node(self.node3))

    def test_add_nodes(self):
        self.node_collection.add_nodes(self.nodes)
        self.assertEqual(len(self.node_collection), 2)
        self.assertIn(self.node1.name, self.node_collection)
        self.assertIn(self.node2.name, self.node_collection)

    def test_remove_node(self):
        self.assertFalse(self.node_collection.remove_node(self.node1))

        self.node_collection.add_node(self.node1)
        self.assertTrue(self.node_collection.remove_node(self.node1))


class TestEdge(unittest.TestCase):
    def setUp(self):
        self.node1 = Node("node1", "data1")
        self.node2 = Node("node2", "data2")
        self.node3 = Node("node3", "data3")
        self.node4 = Node("node4", "data4")

        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node1)
        self.edge3 = Edge(self.node2, self.node3)
        self.edge4 = Edge(self.node3, self.node4)

    def test__init__(self):
        edge = Edge(self.node1, self.node2)
        self.assertEqual(edge.vertex1, self.node1)
        self.assertEqual(edge.vertex2, self.node2)

    def test__eq__(self):
        self.assertEqual(self.edge1, self.edge1)
        self.assertEqual(self.edge1, self.edge2)
        self.assertNotEqual(self.edge1, self.edge3)
        self.assertNotEqual(self.edge2, self.edge3)

    def test_vertices(self):
        self.assertEqual(self.edge1.vertex1, self.node1)
        self.assertEqual(self.edge1.vertex2, self.node2)

    def test_name(self):
        self.assertEqual(self.edge1.name, "node1,node2")

    def test_name_reversed(self):
        self.assertEqual(self.edge1.name_reversed,"node2,node1" )

    def test_connection_exists(self):
        self.assertTrue(self.edge1.connection_exists(self.edge2))
        self.assertFalse(self.edge1.connection_exists(self.edge4))

    def test_vertices(self):
        self.assertIn(self.node1, self.edge1.vertices)
        self.assertIn(self.node2, self.edge1.vertices)
        self.assertNotIn(self.node3, self.edge1.vertices)


class TestEdgeCollection(unittest.TestCase):
    def setUp(self):
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node3")
        self.node4 = Node("node4")
        self.node5 = Node("node5")
        self.node6 = Node("node6")
        self.node7 = Node("node7")

        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node3)
        self.edge3 = Edge(self.node3, self.node4)
        self.edge4 = Edge(self.node4, self.node5)

        self.edge5 = Edge(self.node2, self.node1)
        self.edge6 = Edge(self.node1, self.node5)
        self.edge7 = Edge(self.node6, self.node7)

        self.edges = [self.edge1, self.edge2, self.edge3, self.edge4,
                      self.edge5, self.edge6]

        self.edge_collection = EdgeCollection()

    def fill_collection(self):
        self.edge_collection.add_edges(self.edges)

    def tearDown(self):
        pass

    def test_add_edge(self):
        self.assertTrue(self.edge_collection.add_edge(self.edge1))
        self.assertFalse(self.edge_collection.add_edge(self.edge1))
        self.assertFalse(self.edge_collection.add_edge(self.edge5))

    def test_remove_edge(self):
        self.fill_collection()

        self.assertTrue(self.edge_collection.remove_edge(self.edge1))
        self.assertFalse(self.edge_collection.remove_edge(self.edge1))

    def test_remove_node(self):
        self.fill_collection()
    
        results = self.edge_collection.remove_node(self.node1)
        self.assertIn(self.edge1, results)
        self.assertIn(self.edge6, results)

    def test_add_relationship(self):
        self.fill_collection()

        self.assertIn(self.edge1, self.edge_collection[self.edge2.name])
        self.assertNotIn(self.edge1, self.edge_collection[self.edge3.name])

        self.assertNotIn(self.edge1, self.edge_collection[self.edge1.name][1:])
        self.assertFalse(self.edge_collection.add_relationships(self.edge7))

        # Check to see if adding the same relationship twices creates
        # duplicates.
        self.assertFalse(self.edge_collection.add_relationships(self.edge1))
        self.assertEqual(1, self.edge_collection[self.edge2.name].count(self.edge1))

    def test_remove_relationship(self):
        self.fill_collection()

        # The workflow is to first remove the edge and then remove
        # the relationships.
        self.edge_collection.remove_edge(self.edge1)
        self.assertTrue(self.edge_collection.remove_relationships(self.edge1))
        self.assertNotIn(self.edge1, self.edge_collection[self.edge2.name])


class TestGraph(unittest.TestCase):
    def setUp(self):
        # TODO: add all the nodes, edges, and their respective collections...
        pass

    def tearDown(self):
        pass

    def test_add_node(self):
        pass

    def test_add_nodes(self):
        pass

    def test_add_edge(self):
        pass

    def test_add_edges(self):
        pass

    def test_remove_edge(self):
        pass

    def test_remove_node(self):
        pass

    def test_remove_nodes(self):
        pass


if __name__ == "__main__":
    unittest.main()
