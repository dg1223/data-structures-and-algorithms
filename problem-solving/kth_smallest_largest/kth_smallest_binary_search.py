def count_smaller_than_mid(array, mid):
    count = 0
    for i in range(len(array)):
        if array[i] <= mid:
            count += 1
    return count

def kth_smallest(array, k):
    low = min(array)
    high = max(array)
    while low < high:
        mid = low + (high - low)//2
        count = count_smaller_than_mid(array, mid)
        if count >= k:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    array = [7, 3, 4, 10, 20, 15]
    k = 3
    print(f"{k = }, k-th smallest element = {kth_smallest(array, k)}")