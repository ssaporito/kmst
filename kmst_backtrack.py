from collections import deque
import networkx as nx

def kmst_backtrack(G,k,T,u):
    T=list(T)
    if is_viable(k,T,u):        
        T.append(u)        
        if is_solution(k,T):
            store(G,T)
        else:            
            for v in G[u]:
                kmst_backtrack(G,k,T,v)

def is_solution(k,T):
    return len(T)==k

def is_viable(k,T,u):
    return len(T)<k and u not in T

def store(G,T):
    global results
    r=0
    #print(T)
    for i in range(0,len(T)-1):        
        r+=G[T[i]][T[i+1]]['weight']                        
    results.append([T,r])

def kmst(G,k):
    T=[]
    R=[]        
    n=nx.number_of_nodes(G)
    for i in range(0,n):
        kmst_backtrack(G,k,T,i)
        
results=[]

def test_kmst():
    global results
    G=nx.Graph()
    e=[(0,1,3.0),(1,2,1.0),(0,2,2.0),(0,3,1.0),(3,1,0.5),(1,4,5.0),(2,4,3.0)]
    G.add_weighted_edges_from(e)
    kmst(G,5)    
    print(sorted(results,key=lambda el:el[1])) #print asc sorted results

test_kmst()
    
    
