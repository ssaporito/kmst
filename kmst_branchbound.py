import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *

def kmst_branchbound(G,k,T,V,E):
    global solution_weight
    print(solution_weight)
    if is_viable(k,T,V):
        if is_solution(k,T):
            choose_best_solution(G,T)
        else:
            lower_bound_T=lower_bound(G,k,T)            
            
            if lower_bound_T<solution_weight or solution_weight==float("inf"):                
                print("got here")
                for i in range(0,len(E)):
                    if not V or E[i][0] in V or E[i][1] in V:
                        T2=list(T)
                        E2=list(E)
                        V2=dict(V)
                        V2[E[i][0]]=True
                        V2[E[i][1]]=True
                        T2.append(E2.pop(i))            
                        kmst_branchbound(G,k-1,T2,V2,E2)
            else:
                #print("pruned")
                pass    
                    

def is_viable(k,T,V):    
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

def tree_weight(G,T):
    r=0    
    for t in T:
        r+=G[t[0]][t[1]]['weight']
    return r

def choose_best_solution(G,s2):
    global solutions
    global solution_weight
    weight2=tree_weight(G,s2)
    if solution_weight==float("inf"):
        solutions.append(s2)
        solution_weight=weight2
        return
    weight1=tree_weight(G,solutions[0])    
    if weight1>weight2:
        solutions.clear()
        solutions.append(s2)
        solution_weight=weight2
    elif weight1==weight2:
        solutions.append(s2)    

def lower_bound(G,k,T):
    mst=nx.minimum_spanning_tree(G).edges()
    remainder_mst=mst[:(k-len(T))]
    return tree_weight(G,T+remainder_mst) 
    
