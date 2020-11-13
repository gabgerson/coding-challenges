#undirectied acyclic graph
class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    # def show_connections(self):

    #     for node in self.adjacent_list:
        
    def show_connections(self):
        for node in self.adjacent_list:
            s = f"{node} --> "
            for edge in self.adjacent_list[node]:
                s += f"{edge} "
            print(s)


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.show_connections()