# A graph is a tree structure but with a cycle
# There can be directed (one directional), undirected graph (two directional) and weighted graph (each connection has a weight)
# A directed graph needs to have a direction specified
# undirected graph goes both way (has 2 directions)
# weighted graph is a graph where each connection has a weight, this can we cost, speed, reward, depends on what we are trying to model 
# weighted graph example - what is the shortest path kind of question, where each edge gets assigned a cost, which can we the distance and we need to find which ath leads to the destination with the minimum cost / distance
# Adjacency list is a way of representing a graph in form of a JSON
# Adjaceny Matrix is used to represent directed graph in form of a matrix

# This is an undirected graph implementation
class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict() # Adjacency list

    def __repr__(self):
        graph_str = ""
        for node, neighbours in self.adj_list:
            graph_str += f"{node} -> {neighbours}"
        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node doesnt exist")
        for neighbours in self.adj_list.values():
            neighbours.discard(node) # if key appears in the adj_list then remove it
        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node) # if the start node doesnt exist yet, we first create it before creating the edge
        if to_node not in self.adj_list:
            self.add_node(to_node) # if the destination node doesnt exist yet, we first create it before creating the edge
        if weight is None:
            self.adj_list[from_node].add(to_node) # we add the destination node to the list of from_node
            if not self.directed:
                self.adj_list[to_node].add(from_node) # since this is birectional (undirected) we need to also add connection from the destination to the start node
        else: # we add weight as well
            self.adj_list[from_node].add((to_node, weight)) # we add the destination node to the list of from_node
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight)) # since this is birectional (undirected) we need to also add connection from the destination to the start node


    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list: # check if start node is in the adj list
            if to_node in self.adj_list[from_node]: # check if the end node is part of or neighbour of the start node
                self.adj_list[from_node].remove(to_node) # we remove the connection to the neighbour from the start node
            else:
                raise ValueError('Edge does not exist')
            if not self.directed: # we need to remove edge from both the directions 
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node) # if it is bidrectional we remove edge from both the sides
        else:
            raise ValueError('Edge does not exist')

    def get_neighbours(self, node):
        return self.adj_list.get(node, set()) # gets the node if it exists else returns empty set

    def has_node(self, node):
        return node in self.adj_list # returns True or False

    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node] # returns True or False
        return False

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_node, neighbours in self.adj_list.items(): # we loop through all the start nodes and its neighbours
            for to_node in neighbours: # we fetch all the individual neighbour nodes 
                edges.append((from_node, to_node)) # we append the combination of both individual from and to to get the connection

    def bfs(self, start): # bfs uses queue data structure (FIFO)
        visited = set() # all the node we visited already
        queue = [start] # the starting point in the queue
        order = [] # the order in which we visit the nodes
        while queue: # while there are elements in the queue we need to get the next elements to process
            node = queue.pop(0)
            if node not in visited: # if we havent visited the node yet the we proceed
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node) # we want to get all the neighbours for this node
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple): # for the weighted connection we added tuple right? so here we check if this is a weighted connection or not
                        neighbour = neighbour[0] # we just pick the node
                    if neighbour not in visited: 
                        queue.append(neighbour)
        return order # the first elements added will be the first elements to be processes (FIFO principle), and we return that order


    def dfs(self, start): # bfs uses stack data structure (LIFO)
        visited = set() # all the node we visited already
        stack = [start] # the starting point in the stack
        order = [] # the order in which we visit the nodes
        while stack: # while there are elements in the stack we need to get the next elements to process
            node = stack.pop()
            if node not in visited: # if we havent visited the node yet the we proceed
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node) # we want to get all the neighbours for this node
                for neighbour in sorted(neighbours, reversed=True): # we iterate in the reverse order
                    if isinstance(neighbour, tuple): # for the weighted connection we added tuple right? so here we check if this is a weighted connection or not
                        neighbour = neighbour[0] # we just pick the node
                    if neighbour not in visited: 
                        stack.append(neighbour)
        return order # the last element added will be the first to be processes (LIFO principle), and we return that order



