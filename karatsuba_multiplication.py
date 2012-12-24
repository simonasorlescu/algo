from math import ceil, floor

def multiply (x, y):
    """
        Multiplies x and y recursively by splitting it in two
    """
    sx = str(x)
    sy = str(y)
    n = len(sx)
    m = len(sy)
    x = int(x)
    y = int(y)

    if n is 1 or m is 1:
        if x is 0: x = 10
        if y is 0: y = 10
        return x*y
    else:
        a = int(sx[0:int(floor(n/2))])
        b = int(sx[int(ceil(n/2)):n])
        c = int(sy[0:int(floor(m/2))])
        d = int(sy[int(ceil(m/2)):m])

        ac = multiply(a, c)
        bd = multiply(b, d)
        adbc = multiply(a+b, c+d) - ac - bd
        return ac*(10**2) + adbc*10 + bd


# Test
# import pdb; pdb.set_trace();

#x = 12
#y = 13
#print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)

x = 12
y = 100
print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)

#x = 5678
#y = 1234
#print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)
