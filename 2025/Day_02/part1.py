"""
find invalid id

example:

55 -> 5 twice -> invalid
6464 -> 64 twice -> invalid
etc..

number with leading 0 are invalid

11-22 -> 11,22 invalid
95-115 -> 99 invalid
998-1012 -> 1010 invalid
1188511880-1188511890 -> 1188511885 invalid
222220-222224 -> 222222 invalid
1698522-1698528 -> no invalid
446443-446449 -> 446446 invalid
38593856-38593862 -> 38593859 invalid

answer = sum of all invalid ids
"""

with open("/mnt/c/Users/Asus/Desktop/AOC/2025/Day_02/input.txt") as f:
    id_ranges = [line.strip().split(",") for line in f.readlines()]

invalid_id_sum = 0
for id_range_list in id_ranges:

    for id_range_str in id_range_list:
        id_range = list(map(int, id_range_str.split("-")))
        start_id = id_range[0]
        end_id = id_range[1]

        for current_id in range(start_id, end_id + 1):
            if len(str(current_id)) % 2 ==0 and str(current_id)[:len(str(current_id))//2] == str(current_id)[len(str(current_id))//2:]:
                invalid_id_sum += current_id
            
print(invalid_id_sum)

"""
38310256125

real    0m0.808s
user    0m0.794s
sys     0m0.008s
"""