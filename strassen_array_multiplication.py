def op (x, y, op = '+'):
    """
        Liniar operation over two square, same-size matrices.
        Default is add.
    """
    n = len(x)
    out = []
    for i in range(n):
        line = []
        for j in range(n):
            if op is '+':
                res = x[i][j] + y[i][j]
            elif op is '-':
                res = x[i][j] - y[i][j]
            line.append(res)
        out.append(line)
    return out

def add (x, y):
    """
        Adds two square arrays.
    """
    return op(x, y, '+')

def sub (x, y):
    """
        Subtracts two square arrays.
    """
    return op(x, y, '-')

def strassen_array_multiplication (x, y):
    """
        Multiplies two array using the strassen algorithm.
        Ie. splits x and y into four sectors each:
        x = (a b)   y = (e f)   x*y = (ae+bg af+bh)
            (c d)       (g h)         (cd+dg cf+dh)

        It then computes the 7 strassen coeficients recursively:
        p1 = a(f-h)
        p2 = (a+b)h
        p3 = (c+d)e
        p4 = d(g-e)
        p5 = (a+d)(e+h)
        p6 = (b-d)(g+h)
        p7 = (a-c)(e+f)

        Finally compute x*y components using the strassen coeficients:
        ae+bg = p5 + p4 - p2 + p6
        af+bh = p1 + p2
        ce+dg = p3 + p4
        cf+dh = p1 + p5 - p3 - p7

        @param {Array} x - square array of nxn, where n is a multiple of 2
        @param {Array} y - square array of nxn, where n is a multiple of 2

        NOTE: to make it work for mxn * nxm or for the cases where n is not a
        multiple of 2 a padding of 1s can be added.
    """
    n = len(x) # width/height of both arrays.

    if n is 2:
        a = x[0][0]
        b = x[0][1]
        c = x[1][0]
        d = x[1][1]
        e = y[0][0]
        f = y[0][1]
        g = y[1][0]
        h = y[1][1]

        aebg = a*e + b*g
        afbh = a*f + b*h
        cedg = c*e + d*g
        cfdh = c*f + d*h

        return [
            [aebg, afbh],
            [cedg, cfdh]
        ]

    else:
        m = int(n/2)
        a = x[0:m][0:m]
        b = x[0:m][m+1:n]
        c = x[m+1:n][0:m]
        d = x[m+1:n][m+1:n]
        e = y[0:m][0:m]
        f = y[0:m][m+1:n]
        g = y[m+1:n][0:m]
        h = y[m+1:n][m+1:n]

        p1 = strassen_array_multiplication(a, sub(f, h))
        p2 = strassen_array_multiplication(add(a, b), h)
        p3 = strassen_array_multiplication(add(c, d), e)
        p4 = strassen_array_multiplication(d, sub(g, e))
        p5 = strassen_array_multiplication(add(a, d), add(e, h))
        p6 = strassen_array_multiplication(sub(b, d), add(g, h))
        p7 = strassen_array_multiplication(sub(a, c), add(e, f))

        aebg = add(sub(add(p5, p4), p2), p6)
        afbh = add(p1, p2)
        cedg = add(p3, p4)
        cfdh = sub(sub(add(p1, p5), p3), p7)

        return [
            [aebg, afbh],
            [cedg, cfdh]
        ]


# Test
#x = [[1,2], [3,4]]
#y = [[5,6], [7,8]]
#print strassen_array_multiplication(x, y)

x = [
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6],
    [7,8,9,10]
]
y = [
    [8,9,10,11],
    [9,10,11,12],
    [10,11,12,13],
    [11,12,13,14]
]
print strassen_array_multiplication(x, y)
