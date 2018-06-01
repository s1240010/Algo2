
import queue

#Edge = collections.nametuple("Edge","start end weight")
V = [{}]

def setNode(n):
    global V
    V = [{} for i in range(n)]
def dijkstra(s,t):
    global V
    G = {}
    q = queue.PriorityQueue()
    q.put((0,s))
    while q.empty() == False:
        w,x = q.get()
        if x == t:
            return w
        if w in G:
            continue;
        G[x] = w
        for y in V[x]:
            if(y in G) == False:
                q.put((w + V[x][y],y))
    return None


def main():
    v,e = map(int,input().split())
    setNode(v)
    for i in range(e):
        s,t,w = map(int,input().split())
        V[s][t] = w
    start,goal = map(int,input().split())
    print(dijkstra(start,goal))
if __name__ == '__main__':
    main()
