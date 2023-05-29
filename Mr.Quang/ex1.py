def two_sum(nums, target):
    num_map = {}  # Map to store complement -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return []  # Return empty list if no solution is found

nums = [2, 7, 11, 15]
target = 9

indices = two_sum(nums, target)
if indices:
    print(f"The indices are: {indices}")
else:
    print("No solution found.")
