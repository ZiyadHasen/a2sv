def countingSort(arr):
    res = [0] * 100
    for x in arr:
        res[x] += 1
    return res