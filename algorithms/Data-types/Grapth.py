class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)

            else:
                self.graph_dict[start] = [end]
        # print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in paths:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        all_paths = self.get_paths(start, end)
        shortest_path=[]
        if all_paths:
            shortest=len(all_paths[0])
            shortest_path = all_paths[0]
            for path in all_paths:
                if len(path)<shortest:
                    shortest_path=path
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "dubai"),
        ("paris", "Newyork"),
        ("dubai", "Newyork"),
        ("Newyork", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "mumbai"
    end = "Newyork"
    print(f"Paths between {start} and {end} is :: ", route_graph.get_paths(start, end))
    print(f"Shortest Paths between {start} and {end} is :: ", route_graph.get_shortest_path(start, end))
