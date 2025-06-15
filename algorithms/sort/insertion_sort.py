def insertion_sort(nums):
    for idx, num in enumerate(nums):
        j = idx

        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp

            j -= 1

    return nums
