def clean_string(string):
	return "".join(char for char in string if char.isalnum())

def isPalindrome(string):
	length = len(string)
	if not length:
		return True
	
	clean_str  = clean_string(string)
	clean_str = clean_str.lower()

	return clean_str == clean_str[::-1]

string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))