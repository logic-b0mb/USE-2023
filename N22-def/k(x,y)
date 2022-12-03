def k(x,y):
    if x>y:
        return 0
    if x==y:
        return 1 
    if y%2==0:
        return k(x,y-2) + k(x,y//2)
    return k(x,y-2)
print (k(1,16)*k(16,34))
