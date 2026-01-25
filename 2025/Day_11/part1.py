graph = {}
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_11/input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split(': ')
        node = parts[0]
        edges = parts[1].split(' ') if len(parts) > 1 else []
        graph[node] = edges

def count_paths(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return 1
    visited.add(start)
    path_count = 0
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path_count += count_paths(graph, neighbor, end, visited.copy())
    return path_count

total_paths = count_paths(graph, "you", "out")
print(f"Total paths from you to out: {total_paths}")