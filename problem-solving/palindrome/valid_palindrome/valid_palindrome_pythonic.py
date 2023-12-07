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

	return clean_str == clean_str[::-1]

string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))