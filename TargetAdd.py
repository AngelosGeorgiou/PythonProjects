#given a sorted array of integers 
#return True if there is a couple which adds up to a certain number
#else return False

def addsup(array, target):
	low = 0
	up = len(array)-1
	while low<up:
		total = array[low] + array[up]
		if total == target: return True
		elif total < target: low+=1
		else: up-=1 
	return False

import random
print([(addsup([1,2,3,4,5],i),i) for i in range(1,11)])
a = sorted(random.sample(range(1,2000),59))
print(a)
res = []
for i in range(1,4000): 
	if addsup(a,i): res.append(i)
print(res) 