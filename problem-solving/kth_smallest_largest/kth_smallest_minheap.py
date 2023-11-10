import heapq

def kth_smallest(array, k):
    min_heap = []

    for item in array:
        heapq.heappush(min_heap, item)

    for counter in range(k):
        kth_smallest = heapq.heappop(min_heap)

    return kth_smallest

if __name__ == "__main__":
	arr = [7, 3, 4, 10, 20, 15]
	K = 3

	# Function call
	print("Kth Smallest Element is:", kth_smallest(arr, K))