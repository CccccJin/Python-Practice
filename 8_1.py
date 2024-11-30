def chop(t):
    del t[0]
    del t[-1]
    return None

def middle(list):
    new_list = list[1:-1]
    return list

a = [1,2,3,4,5,6]

print(chop(a))

print(middle(a))
