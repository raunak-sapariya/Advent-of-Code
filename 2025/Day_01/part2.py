"""
actual password -> number of time pointing at 0 (while during rotation and at the end)
dail starts at 50
example:
    L68 -> 82 -> points 0 -> 1
    L30 -> 52 -> points 0 -> no
    R48 -> 0  -> points 0 -> 1
    L5  -> 95 -> points 0 -> no
    R60 -> 55 -> points 0 -> 1
    L55 -> 0  -> points 0 -> 1
    L1  -> 99 -> points 0 -> no
    L99 -> 0  -> points 0 -> 1
    R14 -> 10 -> points 0 -> no
    L82 -> 32 -> points 0 -> 1

    dial pointing at 0 -> 6 times
    password = 6

"""

dial_position = 50
password_counter = 0
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_01/input.txt") as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

for direction, steps in instructions:
    if direction == "L":
        for _ in range(steps):
            dial_position = (dial_position - 1) % 100
            if dial_position == 0:
                password_counter += 1
    elif direction == "R":
        for _ in range(steps):
            dial_position = (dial_position + 1) % 100
            if dial_position == 0:
                password_counter += 1
print(password_counter)

"""
5978

real    0m0.052s
user    0m0.039s
sys     0m0.008s
"""