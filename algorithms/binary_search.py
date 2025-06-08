def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        pos = (low + high) // 2

        if arr[pos] == target:
            return True

        elif arr[pos] > target:
            high = pos - 1

        else:
            low = pos + 1

    return False
