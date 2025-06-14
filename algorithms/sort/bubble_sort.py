# time complexity: O(n^2)
# space complexity: O(1)


def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True

        end -= 1

    return nums
