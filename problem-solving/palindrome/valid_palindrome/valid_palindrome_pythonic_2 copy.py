def isPalindrome(string):
	if not len(string):
		return True
	
	string = "".join(char.lower() for char in string if char.isalnum())    
	return string == string[::-1]

string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))