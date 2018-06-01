import time
import random
random.seed(1234)

def multiMatrix(x,y):
    n = len(x)
    if n == 1:
        return x[0][0] * y[0][0]
    else:
        a = [[col for col in row[:len(row)/2]] for row in x[:len(x)/2]]
        b = [[col for col in row[len(row)/2:]] for row in x[:len(x)/2]]
        c = [[col for col in row[:len(row)/2]] for row in x[len(x)/2:]]
        d = [[col for col in row[len(row)/2:]] for row in x[len(x)/2:]]
        e = [[col for col in row[:len(row)/2]] for row in y[:len(y)/2]]
        f = [[col for col in row[len(row)/2:]] for row in y[:len(y)/2]]
        g = [[col for col in row[:len(row)/2]] for row in y[len(y)/2:]]
        h = [[col for col in row[len(row)/2:]] for row in y[len(y)/2:]]
        ae = multiMatrix(a,e)
        bg = multiMatrix(b,g)
        af = multiMatrix(a,f)
        bh = multiMatrix(b,h)
        ce = multiMatrix(c,e)
        dg = multiMatrix(d,g)
        cf = multiMatrix(c,f)
        dh = multiMatrix(d,h)

        c = [[ae+bg,af+bh],[ce+dg,cf+dh]]

        return c


def createRandomMatrix(n):
        maxVal = 1000 # I don't want to get Java / C++ into trouble
        matrix = []
        for i in xrange(n):
            matrix.append([random.randint(0,maxVal) for el in xrange(n)])
        return matrix


if __name__ == "__main__":
    n = input("Input n:")
    matrixA = createRandomMatrix(n)
    matrixB = createRandomMatrix(n)

    n1 = time.time();
    C = multiMatrix(matrixA,matrixB)
    n2 = time.time();

    elapsed_time = n2-n1
    print elapsed_time
