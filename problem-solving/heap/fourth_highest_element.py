import heapq

def getFourthLargest(arr, n):
    if n < 4:
        return -2147483648

    heap = []

    for num in arr:
        heapq.heappush(heap, -num)

    count = 1
    while heap:
        if count > 4:
            break
        
        fourth_highest = heapq.heappop(heap)

        count += 1

    return -fourth_highest