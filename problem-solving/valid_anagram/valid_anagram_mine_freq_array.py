def increment_index_value(string, array):
	for char in string:
		# get the ascii value of the character
		# ASCII value of 'a' is 97. If you subtract 97
		# from ASCII of 'a', you get 0. This way, b
		# becomes 1, c becomes 2 and so on. We can use
		# this logic to populate our frequency array
		# to count the frequeny of each alphabet
		index = ord(char) - 97
		array[index] += 1

def isAnagram(string_s: str, string_t: str) -> bool:
	if not string_s or not string_t:
		return False

	length_s = len(string_s)
	length_t  = len(string_t)

	if length_s != length_t:
		return False

	# create the frequency arrays for 26 alphabets
	freq_s = [0] * 26
	freq_t = [0] * 26

	# fill up the array (our counter)
	self.increment_index_value(string_s, freq_s)
	self.increment_index_value(string_t, freq_t)

	# now all we need to do is compare the frequencies
	# of each alphabet
	for idx in range(len(freq_s)):
		if freq_s[idx] != freq_t[idx]:
			return False

	return True