import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *

def kmst_backtrack(k,T,V,E):
    if is_viable(k,T,V,E):        
        if is_solution(k,T):
            store(T)
        else:            
            for i in range(0,len(E)):
                if not V or E[i][0] in V or E[i][1] in V:
                    T2=list(T)
                    E2=list(E)
                    V2=dict(V)
                    V2[E[i][0]]=True
                    V2[E[i][1]]=True
                    T2.append(E2.pop(i))            
                    kmst_backtrack(k-1,T2,V2,E2)

def is_viable(k,T,V,E):    
    G=nx.Graph()
    G.add_edges_from(T)
    try:
        nx.find_cycle(G)
        #print("no cycle found")
        return False
    except:
        #print("cycle found")
        return True

def is_solution(k,T):
    return k==1

def store(T):
    global solutions
    solutions.append(T)
    
    
