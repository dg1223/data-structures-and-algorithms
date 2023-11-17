import heapq

'''
Python heapq implements a min-heap. To use it as a max-heap,
we need to push the negative of the input number to the heap.
While returning from the heap, we negate the number again to
get the number with the original sign.
'''
def kth_smallest(array, k):
	# Create a max heap (priority queue)
	max_heap = []

	# Iterate through the array elements
	for number in array:
		# Push the negative of the current element onto the max heap        
		heapq.heappush(max_heap, -number)

		# If the size of the max heap exceeds K, remove the largest element
		if len(max_heap) > k:
			heapq.heappop(max_heap)

	# Return the Kth smallest element (top of the max heap, negated)
	return -max_heap[0]

# Driver's code:
if __name__ == "__main__":
	arr = [7, 3, 4, 10, 20, 15]
	K = 3

	# Function call
	print("Kth Smallest Element is:", kth_smallest(arr, K))
