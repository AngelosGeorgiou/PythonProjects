# You are given an array strarr of strings and an integer k. Your task is to
# return the first longest string consisting of k consecutive strings taken in
# the array.

# #Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas",
# #"theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return
# "".

def longest_consec(strarr, k):
    s = ''
    if k<=0 or len(strarr)==0 or k > len(strarr):
        return ''
    for i in range(0,k):
        s+=strarr[i]
    temp = s
    for i in range(k,len(strarr)):
        temp = temp[len(strarr[i-k]):] + strarr[i]
        if len(temp) > len(s):
            s = temp
    return s
