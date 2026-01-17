"""
the task is to find the maximum possible total power output by selecting two batteries from each line.

example:
987654321111111 -> 98
811111111111119 -> 89
234234234234278 -> 78
818181911112111 -> 92

total power output = 98 + 89 + 78 + 92 = 357
"""

def calculate_total_power(input_lines):
    total_power = 0
    len_lines = len(input_lines)

    for line in input_lines:
        max_two_digit = 0
        n = len(line)
        
        for i in range(n):
            for j in range(i + 1, n):
                two_digit = int(line[i] + line[j])
                if two_digit > max_two_digit:
                    max_two_digit = two_digit
                    
        total_power += max_two_digit

    return total_power

input_lines = []
with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_03/input.txt") as f:
    for line in f:
        input_lines.append(line.strip())
print(calculate_total_power(input_lines))

"""
17193

real    0m0.101s
user    0m0.083s
sys     0m0.004s
"""
