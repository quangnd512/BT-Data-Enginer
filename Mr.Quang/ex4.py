def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array (or equal in size)
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)

    # Perform binary search on the smaller array
    low, high = 0, m
    while low <= high:
        partition_nums1 = (low + high) // 2
        partition_nums2 = (m + n + 1) // 2 - partition_nums1

        max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
        min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]

        max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
        min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]

        if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
            # Found the correct partitions
            if (m + n) % 2 == 0:
                return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
            else:
                return max(max_left_nums1, max_left_nums2)
        elif max_left_nums1 > min_right_nums2:
            # Need to move the partition on nums1 to the left
            high = partition_nums1 - 1
        else:
            # Need to move the partition on nums1 to the right
            low = partition_nums1 + 1

    # Should never reach this point if the input is valid
    raise ValueError("Invalid input or arrays are not sorted")


# Example usage:
nums1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [2, 3, 4]
median = find_median_sorted_arrays(nums1, nums2)
print("Median:", median)
