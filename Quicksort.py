def quick(li):
    leng=len(li)
    if leng<=1:
        return li
    pivot=li[0]
    left=[v for v in li[1:] if pivot>=v]
    right=[v for v in li[1:] if pivot<v]
    return quick(left)+[pivot]+quick(right)