def create_hashmap_of_string(string, hashmap):
	for char in string:
		if char in hashmap:
			hashmap[char] += 1
		else:
			hashmap[char] = 1

def longest_palindrome_length(string):
	length = len(string)
	if length == 1:
		return 1

	hashmap = {}
	create_hashmap_of_string(string, hashmap)

	odd = sum(( 1 for char in hashmap if hashmap[char] % 2 == 1  ))
	# breakpoint()

	return (length - odd + 1) if odd else length

# bbb, ababacd
print(longest_palindrome_length("abc"))