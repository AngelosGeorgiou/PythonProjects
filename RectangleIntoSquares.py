#Cut a rectangle into squares. The output is a a list of the sizes of each
# #square
#   sqInRect(5, 3) should return [3, 2, 1, 1]
#   sqInRect(5, 5) should return None

def sqInRect(lng, wdth):
    if lng == wdth: 
        return None
    def aux(lng1,wdth1):
        x = max(lng1,wdth1)
        y = min(lng1,wdth1)
        if x == 0 or y == 0:
            return []
        return [y]+ aux(x-y,y)

    return aux(lng,wdth)