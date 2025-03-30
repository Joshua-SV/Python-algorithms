class Graph:
    def bfs_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None  # Return None if start or end nodes are missing
    
        visited = set()
        to_visit = [start]
        parent = {start: None}  # Track parents for path reconstruction
    
        while to_visit:
            node = to_visit.pop(0)
            visited.add(node)
    
            if node == end:
                # Reconstruct path using parent dictionary
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]  # Reverse to get correct order
    
            for neighbor in sorted(self.graph[node]):  # Sorted for consistency
                if neighbor not in visited and neighbor not in parent:
                    parent[neighbor] = node  # Store parent before visiting
                    to_visit.append(neighbor)
    
        return None  # If no path is found

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
