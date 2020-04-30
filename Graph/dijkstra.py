import sys
import heapq

class Vertex:
    def __init__(self, id):
        self.id = id
        self.distance = sys.maxsize
        self.previous = None
        self.visited = False
        self.adjacent = {}
    # used for comparing values of vertices in heapq
    def __lt__(self, other_node):
        self_priority = self.distance
        other_priority = other_node.distance
        return self_priority < other_priority

    # used for comparing values of vertices in heapq
    def __gt__(self, other_node):
        self_priority = self.distance
        other_priority = other_node.distance
        return self_priority > other_priority

    ### some setter and getters
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id

    def set_distance(self, distance):
        self.distance = distance
    def get_distance(self):
        return self.distance

    def set_previous(self, prev_obj):
        self.previous = prev_obj
    def get_previous(self):
        return self.previous

    def set_visited(self):
        self.visited = True
    def get_visited(self):
        return self.visited

    def get_adjacent(self):
        return self.adjacent

    def get_weight(self, neighbor_obj):
        return self.adjacent[neighbor_obj]

    def add_neighbor(self, neighbor_obj, weight):
        self.adjacent[neighbor_obj] = weight

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    # adding new vertex
    def add_vertex(self, id):
        self.num_vertices += 1
        new_vertex = Vertex(id)
        self.vert_dict[id] = new_vertex
        return new_vertex

    def get_vertex(self, id):
        if id in self.vert_dict:
            return self.vert_dict[id]
        else:
            return None

    # adding new edge
    # if you want to make it directed graph,
    # simply comment self.vert_dict[to_id].........
    def add_edge(self, from_id, to_id, weight):
        if from_id not in self.vert_dict:
            self.add_vertex(from_id)
        if to_id not in self.vert_dict:
            self.add_vertex(to_id)

        self.vert_dict[from_id].add_neighbor(self.vert_dict[to_id], weight)
        self.vert_dict[to_id].add_neighbor(self.vert_dict[from_id], weight)

    def get_vertices(self):
        return self.vert_dict.keys()

class Dijkstra(object):

    def __init__(self, graph):
        self.graph = graph

    # method to use for getting optimum path to a node
    def shortest(self, v, path_list):
        if v:
            path_list.append(v.get_id())
            self.shortest(v.get_previous(), path_list)
        return path_list

    # main algorithm goes here
    def calculate_path(self, start_id):

        h = []
        start_vertex = self.graph.get_vertex(start_id)
        start_vertex.set_distance(0)

        # pushing new item to the heap
        heapq.heappush(h, start_vertex)
        while h:
            u = heapq.heappop(h)
            u.set_visited()
            for v in u.get_adjacent():
                # if v is already visited, we continue
                if v.get_visited():
                    continue

                # getting the weight of the edge
                weight = u.adjacent[v]

                # calculating previous distance + edge value
                new_distance = u.get_distance() + weight

                # if new distance is less than the current node's distance
                if new_distance < v.get_distance():
                    v.set_previous(u)
                    v.set_distance(new_distance)
                    heapq.heappush(h, v)

    # method for calculating the shortest path to a target vertex
    def get_shortest_path_to(self, id):
        target_vertex = self.graph.get_vertex(id)
        print('shortest path to the node %s is:' %target_vertex.get_id(), target_vertex.get_distance())
        shortest_path = self.shortest(target_vertex, [])

        return shortest_path

if __name__ == '__main__':

    my_graph = Graph()

    my_graph.add_vertex('a')
    my_graph.add_vertex('b')
    my_graph.add_vertex('c')
    my_graph.add_vertex('d')
    my_graph.add_vertex('e')
    my_graph.add_vertex('f')
    my_graph.add_vertex('g')

    my_graph.add_edge('a', 'b', 5)
    my_graph.add_edge('b', 'c', 1)
    my_graph.add_edge('c', 'd', 1)
    my_graph.add_edge('c', 'f', 2)
    my_graph.add_edge('d', 'e', 2)
    my_graph.add_edge('f', 'g', 2)
    my_graph.add_edge('a', 'f', 1.5)

    dij = Dijkstra(my_graph)
    dij.calculate_path('a')

    path_b = dij.get_shortest_path_to('b')
    path_c = dij.get_shortest_path_to('c')
    path_d = dij.get_shortest_path_to('d')
    path_e = dij.get_shortest_path_to('e')
    path_f = dij.get_shortest_path_to('f')
    path_g = dij.get_shortest_path_to('g')








