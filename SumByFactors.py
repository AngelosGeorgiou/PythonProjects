# Given an array of positive or negative integers

# I= [i1,..,in]

# you have to produce a sorted array P of the form

# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij]
# [ [...]


def sum_for_list(lst):
	primes=[2]
	limit = abs(min(lst)) if abs(min(lst)) > max(lst) else max(lst)
	for num in range(3,limit+1,2):
		notPrime = False
		for prime in primes:
			if num/2<prime: break
			if num%prime == 0:
				notPrime = True
				break
		if not notPrime: primes.append(num)
	print(primes)
	factors = dict()
	for num in lst:
		if abs(num) in primes:
			try:
				factors[abs(num)] += num
			except KeyError as e:
				factors[abs(num)] = num
			continue
		for prime in primes:
			if num%prime==0:
				try:
					factors[prime] += num
				except KeyError as e:
					factors[prime] = num

			if prime>abs(num): break
	return sorted([[key, value] for key, value in factors.items()])


# a=[107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
# print(sum_for_list(a))
