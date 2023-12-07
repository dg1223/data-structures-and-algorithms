# O(N) time, O(1) space

def isPalindrome(string: str) -> bool:
	if not len(string):
		return True

	head = 0
	tail = len(string) - 1

	while head < tail:
		head_str, tail_str = string[head].lower(), string[tail].lower()

		is_head_alnum = head_str.isalnum()
		is_tail_alnum = tail_str.isalnum()

		if is_head_alnum and is_tail_alnum:
			if head_str != tail_str:
				return False
			head += 1
			tail -= 1
		elif not is_head_alnum:
			head += 1
		elif not is_tail_alnum:
			tail -= 1
	return True

string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))