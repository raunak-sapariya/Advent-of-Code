tachyon = []
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_07/input.txt") as f:
    for line in f:
        if line.strip():
            tachyon.append(list(line.strip()))

total_split = 0
for i in range(len(tachyon)):
    for j in range(len(tachyon[i])):
        if tachyon[i][j] == 'S':
            if i + 1 < len(tachyon):
                tachyon[i+1][j] = '|'

        elif tachyon[i][j] == '^':
            if i -1 >=0 and tachyon[i-1][j] == '|':
                total_split +=1

            #left beam
            if j - 1 >= 0 and tachyon[i][j-1] == '.':
                tachyon[i][j-1] = '|'
                # continue left beam
                if i + 1 < len(tachyon) and tachyon[i+1][j-1] == '.':
                    tachyon[i+1][j-1] = '|'

            #right beam
            if j + 1 < len(tachyon[i]) and tachyon[i][j+1] == '.':
                tachyon[i][j+1] = '|'
                # continue right beam
                if i + 1 < len(tachyon) and tachyon[i+1][j+1] == '.':
                    tachyon[i+1][j+1] = '|'

        elif tachyon[i][j] == '|':
            # continue the beam down if .
            if i + 1 < len(tachyon) and tachyon[i+1][j] == '.':
                tachyon[i+1][j] = '|'

# for i in range(len(tachyon)):
#         for j in range(len(tachyon[i])):
#             print(tachyon[i][j], end="  ")
#         print()

print(total_split)

"""
1630

real    0m0.022s
user    0m0.012s
sys     0m0.000s
"""
