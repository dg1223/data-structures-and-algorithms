def sort_array(array):
    # perform selection sort: O(N^2)
    # or use the sort() function for O(NlogN)
    length = len(array)
    for idx_1 in range(length):
        for idx_2 in range(idx_1+1, length):
            if array[idx_1] > array[idx_2]:
                array[idx_1], array[idx_2] = array[idx_2], array[idx_1]

def kth_smallest(array, k):
    # sort array
    sort_array(array)
    return array[k-1]

array = [7, 10, 4, 3, 20, 15]
k = 4
kth_smallest = kth_smallest(array, k)
print(f"{k = }, {kth_smallest = }")
    