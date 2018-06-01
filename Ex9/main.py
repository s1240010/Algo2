import sys

def MatrixChainOrder(r,n):
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for L in range(1,n):
        for i in range(0,n-L):
            j=i+L
            m[i][j]=sys.maxint
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+r[i]*r[k+1]*r[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

def PrintOptimalParens(s,i,j):
    if(i==j):
        print "A",
    else:
        print "(",
        PrintOptimalParens(s,i,s[i][j])
        PrintOptimalParens(s,s[i][j]+1,j)
        print ")",

if __name__ == '__main__':
    r = list(map(int,raw_input("Please input sequence : ").split(",")))
    n=len(r)-1
    m,s=MatrixChainOrder(r,n)
    print "The optimal parenthesization for those matrices costs: ",
    print m[0][n-1]
    print "The optimal parens:  ",
    PrintOptimalParens(s,0,n-1)
    print
