from operator import mul, add
from functools import reduce

input_data = []

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_06/sample.txt") as f:
    input_data = [line.strip().split() for line in f if line.strip()]

transposed_data = zip(*input_data)

total = []
for data in transposed_data:
    operator = data[-1]
    values = [int(item) for item in data[:-1]]
    print(operator, values)
    
    if operator == '*':
        total.append(reduce(mul, values, 1))
    elif operator == '+':
        total.append(sum(values))

print(sum(total))

"""
5524274308182

real    0m0.023s
user    0m0.010s
sys     0m0.006s
"""