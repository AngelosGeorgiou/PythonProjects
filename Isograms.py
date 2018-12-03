# An isogram is a word that has no repeating letters, consecutive or non-
# consecutive. Implement a function that determines whether a string that
# contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.

def is_isogram(string):
	s = sorted(string.lower())
	for i in range(0,len(string)-1):
		if s[i] == s[i+1]:
			return False
	return True