spoiled_item = set()
ranges = []

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_05/input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if "-" in line:
            start, end = line.split("-")
            ranges.append((int(start.strip()), int(end.strip())))
        else:
            spoiled_item.add(int(line))

fresh_item = set()
for start, end in ranges:
    for num in spoiled_item:
        if start <= num <= end:
            fresh_item.add(num)

print(len(fresh_item))

"""
525

real    0m0.028s
user    0m0.019s
sys     0m0.004s
"""
