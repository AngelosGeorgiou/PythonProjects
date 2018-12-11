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


hive = ["bee.bee",
        ".e..e..",
        ".b..eeb"]

print(how_many_bees(hive))
