junction_box = []

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_08/input.txt") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(','))
        junction_box.append((x, y, z))

def find_distance(p1:list, p2:list) -> int:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

all_points_with_distances = []

def total_distance(junctions:list) -> float:
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            dist = find_distance(junctions[i], junctions[j])
            all_points_with_distances.append((dist, i, j))
    return all_points_with_distances

def sort_distances(distances:list) -> list:
    return sorted(distances, key=lambda item: item[0], reverse=False)

edges = sort_distances(total_distance(junction_box))

circuits = [{i} for i in range(len(junction_box))]

# 10 for sample, 1000 for input
for i in range(1000):
    dist, a, b = edges[i]
    set_a = None
    set_b = None
    for s in circuits:
        if a in s:
            set_a = s
        if b in s:
            set_b = s
    if set_a != set_b:
        circuits.remove(set_a)
        circuits.remove(set_b)
        circuits.append(set_a.union(set_b))

size = sorted([len(c) for c in circuits], reverse=True)

print(size[0] * size[1] * size[2])

"""
75680

real    0m0.508s
user    0m0.432s
sys     0m0.068s
"""
