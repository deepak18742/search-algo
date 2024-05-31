def ternary_search(ar, l, r, x):
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        
        if ar[mid1] == x:
            return mid1
        
        if ar[mid2] == x:
            return mid2
        
        if x < ar[mid1]:
            return ternary_search(ar, l, mid1 - 1, x)
        elif x > ar[mid2]:
            return ternary_search(ar, mid2 + 1, r, x)
        else:
            return ternary_search(ar, mid1 + 1, mid2, x)
    
    return -1

