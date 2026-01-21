"""
. . . . . . . S . . . . . . . 
. . . . . . . | . . . . . . .
. . . . . . . ^ . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . ^ . ^ . . . . . .
. . . . . . . . . . . . . . .
. . . . . ^ . ^ . ^ . . . . .
. . . . . . . . . . . . . . .
. . . . ^ . ^ . . . ^ . . . .
. . . . . . . . . . . . . . .
. . . ^ . ^ . . . ^ . ^ . . .
. . . . . . . . . . . . . . .
. . ^ . . . ^ . . . . . ^ . .
. . . . . . . . . . . . . . .
. ^ . ^ . ^ . ^ . ^ . . . ^ .
. . . . . . . . . . . . . . .

.  .  .  .  .  .  .  S  .  .  .  .  .  .  .  
.  .  .  .  .  .  .  1  .  .  .  .  .  .  .  
.  .  .  .  .  .  1  ^  1  .  .  .  .  .  .  
.  .  .  .  .  .  1  .  1  .  .  .  .  .  .  
.  .  .  .  .  1  ^  2  ^  1  .  .  .  .  .  
.  .  .  .  .  1  .  2  .  1  .  .  .  .  .  
.  .  .  .  1  ^  3  ^  3  ^  1  .  .  .  .
.  .  .  .  1  .  3  .  3  .  1  .  .  .  .
.  .  .  1  ^  4  ^  3  3  1  ^  1  .  .  .
.  .  .  1  .  4  .  3  3  1  .  1  .  .  .
.  .  1  ^  5  ^  4  3  4  ^  2  ^  1  .  .  
.  .  1  .  5  .  4  3  4  .  2  .  1  .  .
.  1  ^  1  5  4  ^  7  4  .  2  1  ^  1  .
.  1  .  1  5  4  .  7  4  .  2  1  .  1  .
1  ^  2  ^  A  ^  B  ^  B  ^  2  1  1  ^  1
1  .  2  .  10  .  11  .  11  .  2  1  1  .  1

1 + 2 + 10 + 11 + 11 + 2 + 1 + 1 + 1 = 40

total_timelines = 40
"""

tachyon = []
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_07/input.txt") as f:
    for line in f:
        if line.strip():
            tachyon.append(list(line.strip()))

for i in range(len(tachyon)):
    for j in range(len(tachyon[i])):

        if tachyon[i][j] == 'S':
            if i + 1 < len(tachyon):
                tachyon[i+1][j] = 1

        elif tachyon[i][j] == '^':

            if isinstance(tachyon[i-1][j], int):
                incoming = tachyon[i-1][j]

                #left beam
                if j - 1 >= 0:
                    # previous beam split
                    if isinstance(tachyon[i][j-1], int):
                        tachyon[i][j-1] += incoming
                    else:
                        tachyon[i][j-1] = incoming
                    # continue left beam
                    if i + 1 < len(tachyon):
                        if isinstance(tachyon[i+1][j-1], int):
                            tachyon[i+1][j-1] = tachyon[i][j-1]
                        elif tachyon[i+1][j-1] == '.':
                            tachyon[i+1][j-1] = tachyon[i][j-1]

                #right beam
                if j + 1 < len(tachyon[i]):
                    # previous beam split
                    if isinstance(tachyon[i][j+1], int):
                        tachyon[i][j+1] += incoming
                    else:
                        tachyon[i][j+1] = incoming
                    # continue right beam
                    if i + 1 < len(tachyon):
                        if isinstance(tachyon[i+1][j+1], int):
                            tachyon[i+1][j+1] += tachyon[i][j+1]
                        elif tachyon[i+1][j+1] == '.':
                            tachyon[i+1][j+1] = tachyon[i][j+1]

        # continue the beam down if .
        elif isinstance(tachyon[i][j], int):
            if i + 1 < len(tachyon) and tachyon[i+1][j] == '.':
                tachyon[i+1][j] = tachyon[i][j]

# for i in range(len(tachyon)):
#         for j in range(len(tachyon[i])):
#             print(tachyon[i][j], end="  ")
#         print()

total_timelines = 0
for j in range(len(tachyon[0])):
    if isinstance(tachyon[-1][j], int):
        total_timelines += tachyon[-1][j]

print(total_timelines)

"""
47857642990160

real    0m0.024s
user    0m0.009s
sys     0m0.009s
"""
