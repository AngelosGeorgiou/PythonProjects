#Write a function called that takes a string of parentheses, and determines if
#the order of the parentheses is valid. The function should return true if the
#string is valid, and false if it's invalid.

def valid_parentheses(string):
    total = 0
    for letter in string:
        if letter=='(':
            total+=1
        elif letter == ')':
            total-=1
        if total < 0:
            return False
    return total == 0