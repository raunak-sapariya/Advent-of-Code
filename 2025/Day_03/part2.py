"""
the task is to find the maximum possible total power output by selecting 12 batteries from each line.
total_digit = 15
batteries = 12
toatal_removal = 15 - 12 = 3
example:
987654321111111 -> 987654321111 -> (987654321111***)
811111111111119 -> 811111111119 -> (81111111111***9)
234234234234278 -> 434234234278 -> (**4*34234234278)
818181911112111 -> 888911112111 -> (8*8*8*911112111)

if found smaller digit remove it until removed 3 digits.

total power output = 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
"""

def max_k_digits(s: str, k:int = 12) -> str:
    n =  len(s)
    total_removal = n - k
    # print(f"Total removal needed: {total_removal}")
    stack = []

    for digits in s:
        while stack and total_removal > 0 and stack[-1] < digits:
            removed = stack.pop()
            total_removal -= 1
        stack.append(digits)
        # print(f"Added {digits}, stack: {stack}")
            

    if len(stack) > k:
        stack = stack[:k]

    result = ''.join(stack)
    # print(f"Max {k} digits from {s} is: {result}")
    return result


with open("/mnt/c/Users/Asus/Desktop/AOC/Day_03/input.txt") as f:
    total_joltage =0
    for line in f:
       joltag = max_k_digits(line.strip(), 12)
       total_joltage += int(joltag)

    print(total_joltage)

"""
171297349921310

real    0m0.030s
user    0m0.009s
sys     0m0.005s
"""

