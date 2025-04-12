arr = [7, 1, 5, 3, 9]
k = 2
arr_sorted = [1, 3, 5, 7, 9]
def kth_max_min(arr, k):
    arr_sorted = sorted(arr)
    return arr_sorted[k-1], arr_sorted[-k]

