# time complexity: O(n log n)
# space complexity: O(n)


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    split_idx = len(nums) // 2

    first = nums[:split_idx]
    second = nums[split_idx:]

    sorted_first = merge_sort(first)
    sorted_second = merge_sort(second)

    return merge(sorted_first, sorted_second)


def merge(first, second):
    final = []
    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1

        else:
            final.append(second[j])
            j += 1

    if i < len(first):
        final += first[i:]

    elif j < len(second):
        final += second[j:]

    return final
