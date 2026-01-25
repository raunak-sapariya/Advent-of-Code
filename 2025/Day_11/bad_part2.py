graph = {}
with open("2025/Day_11/input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split(': ')
        node = parts[0]
        edges = parts[1].split(' ') if len(parts) > 1 else []
        graph[node] = edges

def count_paths(start, end, must_visit, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        if must_visit.issubset(visited):
            print(f"Valid")
            return 1
        else:
            return 0
    new_visited = visited | {start}
    path_count = 0
    for neighbor in graph.get(start, ()):
        if neighbor not in new_visited:
            path_count += count_paths(neighbor, end, must_visit, new_visited)
    return path_count

total_paths = count_paths("svr", "out", {"dac", "fft"})
print(f"Total paths from svr to out: {total_paths}")
