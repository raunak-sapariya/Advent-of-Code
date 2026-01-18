"""
find the number of "@" symbols that are not adjacent to 4 or more other "@" symbols
"""
rolls = []
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_04/input.txt") as f:
    for line in f:
        rolls.append(line.strip())

count = 0
total = 0

for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        current = rolls[i][j]
        # print(f"Checking position {i}, {j} with value {current}")
        if current == "@":
            if len(rolls[i]) > j+1 and rolls[i][j+1] == "@": #right
                #print(f"    Found at {i}, {j+1} going right")
                count += 1
            if j-1 >= 0 and rolls[i][j-1] == "@": #left
                #print(f"    Found at {i}, {j-1} going left")
                count += 1
            if len(rolls) > i+1 and rolls[i+1][j] == "@": #down
                #print(f"    Found at {i+1}, {j} going down")
                count += 1
            if len(rolls) > i+1 and j-1 >= 0 and rolls[i+1][j-1] == "@": #down_left
                #print(f"    Found at {i+1}, {j-1} going down left")
                count += 1
            if len(rolls) > i+1 and len(rolls[i+1]) > j+1 and rolls[i+1][j+1] == "@": #down_right
                #print(f"    Found at {i+1}, {j+1} going down right")
                count += 1
            if i-1 >= 0 and rolls[i-1][j] == "@": #up
                #print(f"    Found at {i-1}, {j} going up")
                count += 1
            if i-1 >= 0 and j-1 >= 0 and rolls[i-1][j-1] == "@": #up_left
                #print(f"    Found at {i-1}, {j-1} going up left")
                count += 1
            if i-1 >= 0 and len(rolls[i-1]) > j+1 and rolls[i-1][j+1] == "@": #up_right
                #print(f"    Found at {i-1}, {j+1} going up right")
                count += 1
                
        total += 1 if count < 4 and rolls[i][j] == "@" else 0
        count = 0

print(total)

"""
1551

real    0m0.042s
user    0m0.022s
sys     0m0.005s
"""
