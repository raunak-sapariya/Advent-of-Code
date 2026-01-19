ranges = []

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_05/input.txt") as f:
    for line in f:
        line = line.strip()
        if line and "-" in line:
            start, end = line.split("-")
            ranges.append((int(start.strip()), int(end.strip())))

ranges.sort()
merged = []

for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total = sum(end - start + 1 for start, end in merged)
print(total)

"""
333892124923577

real    0m0.023s
user    0m0.004s
sys     0m0.008s
"""
