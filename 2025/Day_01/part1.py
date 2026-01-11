"""
0-99 in number in order moves in circle.
L -> moves toward lower number
R -> moves toward higher number

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90
91 92 93 94 95 96 97 98 99
example:

pointing at 11
    R8 -> pointing at 19
    L19 -> pointing at 0

pointing at 5
    L10 -> pointing at 95
    R5 -> pointing at 0

password -> number of times left pointng at 0

Pointing at 50
    L68 -> 82
    L30 -> 52
    R48 -> 0
    L5  -> 95
    R60 -> 55
    L55 -> 0
    L1  -> 99
    L99 -> 0
    R14 -> 10
    L82 -> 32

    dial pointing at 0 -> 3 times
    password = 3
"""
dial_position = 50
password_counter = 0

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_01/input.txt") as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

for direction, steps in instructions:
    if direction == "L":
        dial_position = (dial_position - steps) % 100
    elif direction == "R":
        dial_position = (dial_position + steps) % 100
    if dial_position == 0:
        password_counter += 1
print(password_counter)

"""
997

real    0m0.021s
user    0m0.010s
sys     0m0.005s
"""