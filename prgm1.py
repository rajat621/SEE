matrix = [
 [1, 3, 5],
 [2, 6, 9],
 [3, 6, 9]
]
def matrix_median(matrix):
    import bisect
    low, high = 1, 10**9
    n, m = len(matrix), len(matrix[0])
    while low < high:
        mid = (low + high) // 2
        count = 0
        for row in matrix:
            count += bisect.bisect_right(row, mid)
        if count < (n * m) // 2 + 1:
            low = mid + 1
        else:
            high = mid
    return low
