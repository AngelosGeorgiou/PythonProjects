#There is an array with some numbers. All numbers are equal except for one.
#Try to find it!

def find_uniq(arr):
    return [i for i in arr if i!=arr[0]][0] if arr[1] == arr[0] else arr[1] if arr[2] == arr[0] else arr[0] 
