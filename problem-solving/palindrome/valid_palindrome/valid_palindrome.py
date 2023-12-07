def clean_string(string):
	clean = ""
	for idx in range(len(string)):
		if string[idx].isalnum():
			clean += string[idx]
	return clean

def isPalindrome(string):
	length = len(string)
	if not length:
		return True
	
	clean_str  = clean_string(string)
	clean_str = clean_str.lower()

	head = 0
	tail = len(clean_str) - 1
	while head < tail:
		if clean_str[head] != clean_str[tail]:
			return False
		head += 1
		tail -= 1
	return True

string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))