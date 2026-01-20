input_data = []

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_06/input.txt") as f:
    input_data = [line.rstrip("\n") for line in f if line.strip()]

transposed_data = list(zip(*input_data))[::-1]
total = []

problems = []
current_problem = []

for col in transposed_data:
    if all(c == ' ' for c in col):
        if current_problem:
            problems.append(current_problem)
            current_problem = []
    else:
        current_problem.append(col)
if current_problem:
    problems.append(current_problem)


for problem in problems:
    operator = problem[-1][-1]

    values = []
    for col in problem:
        num_str = ''.join(c for c in col if c not in ['+', '*', ' '])
        if num_str:
            values.append(int(num_str))
    
    if operator == '*':
        prod = 1
        for num in values:
            prod *= num
        total.append(prod)
    elif operator == '+':
        summ = 0
        for num in values:
            summ += num
        total.append(summ)

print(sum(total))

"""
8843673199391

real    0m0.022s
user    0m0.010s
sys     0m0.006s
"""