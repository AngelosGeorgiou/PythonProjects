# You are given an array (which will have a length of at least 3, but could be
# very large) containing integers. The array is either entirely comprised of
# odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns
# this "outlier" N.

def find_outlier(integers):
    odd = even = 0
    for i in [0,1,2]:
        if integers[i]%2 == 0:
            even += 1
        else:
            odd += 1
    k = 1 if even > odd else 0
    for i in integers:
        if i%2==k:
            return i
    return None