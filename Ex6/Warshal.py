V, E = map(int, input().split())
d = [[0 for i in range(V)] for j in range(V)]


for i in range(E):
    s, t = map(int,input().split())
    d[s][t] = 1


for i in range(V):
    for j in range(V):
        if(i == j or d[i][j] == 1):
            d[i][j] = 1
        else:
            d[i][j] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = d[i][j] or (d[i][k] and d[k][j])

for di in d:
    print(di)
