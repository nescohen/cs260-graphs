#!/usr/bin/env python3
# 
# Nes Cohen
# Graph Lab
# CS 260 Data Structures
#

import random as r
from pprint import pprint

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

    # Implementation of Dijkstra's shortest path algorithm
    # only returns length of path, not nodes
    def dijkstras(self, start, destination):
        unvisited = list(self.nodes.keys())
        distance = {nodeId: 0 if nodeId == start else float('inf') 
                        for (nodeId, _) in self.nodes.items()}
        curr = start
        while True:
            if curr == destination or min(unvisited) == float('inf'):
                break
            currEdges = filter(
                           lambda edge: True if edge[0] == curr else False,
                           self.edges)
            for (_from, to, weight) in currEdges:
                newDistance = distance[curr] + weight
                if newDistance < distance[to]:
                    distance[to] = newDistance
            unvisited.remove(curr)
            curr = min(unvisited, key=distance.get)
        return distance[destination]

    # Implementation of Prim's algorithm assuming all edges are unidirectional
    # Returns a new graph representing the MST
    def prims(self):
        result = Graph()
        rmap = {}
        unconnected = list(self.nodes.keys())
        cost = {nodeId: float('inf') for (nodeId, _) in self.nodes.items()}
        connection = {nodeId: None for (nodeId, _) in self.nodes.items()}
        while True:
            if len(unconnected) <= 0:
                break
            curr = min(unconnected, key=cost.get)
            unconnected.remove(curr)
            newCurr = result.addNode(curr)
            rmap[curr] = newCurr
            if connection[curr] != None:
                e = connection[curr]
                dest = e[0] if e[1] == curr else e[1]
                result.addEdge(newCurr, dest, 1)
                result.addEdge(dest, newCurr, 1)
            for edge in filter(lambda e: e[0] == curr or e[1] == curr, self.edges):
                other = edge[0] if edge[1] == curr else edge[1]
                weight = edge[2]
                if other in unconnected and weight < cost[other]:
                    cost[other] = weight
                    connection[other] = edge
        return result


# First create an example graph with a couple of nodes
print("Creating a graph with 2 nodes A and B")
g = Graph()
aId = g.addNode("A")
bId = g.addNode("B")

# Test no edge case of dijkstras
print("Shortest path with no edges:")
print(g.dijkstras(aId, bId))

# Test single edge case
g.addEdge(aId, bId, 1)
print("Shortest path with a single edge of weight 1:")
print(g.dijkstras(aId, bId))

# Test chain case
cId = g.addNode("C")
dId = g.addNode("D")
eId = g.addNode("E")
g.addEdge(bId, cId, 1)
g.addEdge(cId, dId, 1)
g.addEdge(dId, eId, 1)
print("Shortest path, chain of 4 1-weight edges:")
print(g.dijkstras(aId, eId))

# Random graph test
rg = Graph()
for i in range(0, 10):
    rg.addNode(str(i))
print("Random graph test:")
print("Nodes:")
pprint(rg.nodes)
nodeList = list(rg.nodes.keys())
for i in range(0, r.randint(10, 30)):
    fromNode = r.choice(nodeList)
    toNode = r.choice(nodeList)
    weight = r.randint(0, 10)
    rg.addEdge(fromNode, toNode, weight)
print("Edges (from, to, weight):")
pprint(rg.edges)
print("Three randomly chosen paths:")
for i in range(0, 3):
    start = r.choice(nodeList)
    stop = r.choice(nodeList)
    print("Shortest path from " +
            rg.nodes[start] + " to " + rg.nodes[stop] + ":")
    print(rg.dijkstras(start, stop))
print("Prim's algorithm to find minimum spanning tree of random graph")
mst = rg.prims()
print("Nodes:")
pprint(mst.nodes)
print("Edges (from, to, weight):")
pprint(mst.edges)
