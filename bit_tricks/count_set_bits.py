# Count set bits in an integer
# Function to get no of set bits in binary
# representation of passed binary no. */
def countSetBits(n):
	count = 0
	while (n):
		n &= (n-1) 
		count+= 1
	
	return count

# test
i = 9
print(countSetBits(i))
