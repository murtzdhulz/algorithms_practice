__author__ = 'Murtaza'

def product_recurse(small,big):
    if small==0:
        return 0
    elif small==1:
        return big
    s=small>>1
    halfprod = product_recurse(s,big)
    if small%2==0:
        return halfprod+halfprod
    else:
        return halfprod+halfprod+big

def product(a,b):
    small=a if a<b else b
    big=a if a>b else b
    return product_recurse(small,big)

print product(7,7)