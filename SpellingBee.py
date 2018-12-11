# How many bees are in the beehive?

#     bees can be facing UP, DOWN, LEFT, or RIGHT
#     bees can share parts of other bees

# Examples

# Ex1

# bee.bee     
# .e..e..
# .b..eeb

# Answer: 5

def how_many_bees(hive):
	if len(hive) == 0: return 0
	def hmb(hive):
		total = 0
		aux = list()
		for x in hive:
			aux.append("".join(x))
		for x in aux:
			total+=x.count('bee')
			total+=x[::-1].count('bee')
		return total
	return hmb(hive) + hmb(zip(*hive))


#Better solutions 
#https://www.codewars.com/kata/reviews/5920efb0736ad71291000390/groups/59229b634a235f93eb000da5
def count(it):
    return sum(''.join(x).count('bee') + ''.join(x).count('eeb') for x in it)

def how_many_bees(hive):
    return count(hive) + count(zip(*hive)) if hive else 0