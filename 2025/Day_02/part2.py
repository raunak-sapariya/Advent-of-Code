"""
find invalid id

example:
55 -> 5 twice -> invalid
6464 -> 64 twice -> invalid
12341234 -> 1234 twice -> invalid
123123123 -> 123 thrice -> invalid
1212121212 -> 12 five times -> invalid
1111111 -> 1 seven times -> invalid
etc..

11-22 -> 11,22 invalid
95-115 -> 99,111 invalid
998-1012 -> 999,1010 invalid
1188511880-1188511890 -> 1188511885 invalid
222220-222224 -> 222222 invalid
1698522-1698528 -> no invalid
446443-446449 -> 446446 invalid
38593856-38593862 -> 38593859 invalid
565653-565659 -> 565656 invalid
824824821-824824827 -> 824824824 invalid
2121212118-2121212124 -> 2121212121 invalid

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
            current_id_str = str(current_id)
            length = len(current_id_str)
            # print("checking id:", current_id)
            # print("length:", length)
            # print(length // 2 + 1) 

            for size in range(1, length // 2 + 1):
                # print("  size:", size)

                if length % size == 0:
                    times = length // size
                    # print("    times:", times)

                    if current_id_str[:size] * times == current_id_str:
                        # print("    invalid id found:", current_id)
                        invalid_id_sum += current_id
                        break
print(invalid_id_sum)

"""
58961152806

real    0m1.561s
user    0m1.551s
sys     0m0.004s
"""