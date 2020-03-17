# 
# Nes Cohen
# Graph Lab
# CS 260 Data Structures
#

# Class Graph defines a directed, weighted, multigraph with arbitrarily labeled nodes
# Also includes implementation of dijkstra's shortest path and minimum spanning tree algorithms
class Graph:

    # Initialize only as empty graph
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.nextId = 0

    # Add a node, function returns the node's ID
    def addNode(self, label):
        nodeId = self.nextId
        self.nextId += 1
        self.nodes[nodeId] = label
        return nodeId

    # Add an edge, referenced nodes must already exist
    # Returns True if successfully insert, else false
    def addEdge(self, fromNode, toNode, weight):
        if fromNode in self.nodes and toNode in self.nodes:
            self.edges.append((fromNode, toNode, weight))
            return True
        else:
            return False

    
        
        

