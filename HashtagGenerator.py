
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


def generate_hashtag(s):
	return False if len(s) == 0 else '#'+"".join(word.title() for word in s.split()) if len(s.replace(" ",""))<140 else False 

