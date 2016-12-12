import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *

def kmst_branchbound(G,k,T,V,E,solutions,solution_weight_holder):
    solution_weight=solution_weight_holder[0]
    if is_viable(k,T,V):
        if is_solution(k,T):
            choose_best_solution(G,T,solutions,solution_weight_holder)
        else:
            lower_bound_T=lower_bound(G,k,T)                        
            if lower_bound_T<solution_weight or solution_weight==float("inf"):                                
                for i in range(0,len(E)):
                    if not V or E[i][0] in V or E[i][1] in V:
                        T2=list(T)
                        E2=list(E)
                        V2=dict(V)
                        V2[E[i][0]]=True
                        V2[E[i][1]]=True
                        T2.append(E2.pop(i))            
                        kmst_branchbound(G,k-1,T2,V2,E2,solutions,solution_weight_holder)
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

def choose_best_solution(G,s2,solutions,solution_weight_holder):
    solution_weight=solution_weight_holder[0]
    weight2=tree_weight(G,s2)
    if solution_weight==float("inf"):
        solutions.append(s2)
        solution_weight=weight2
        solution_weight_holder[0]=solution_weight
        return
    weight1=solution_weight   
    if weight1>weight2:
        solutions.clear()
        solutions.append(s2)
        solution_weight=weight2
        solution_weight_holder[0]=solution_weight
    elif weight1==weight2:
        solutions.append(s2)    

def lower_bound(G,k,T):
    mst=nx.minimum_spanning_tree(G).edges()
    remainder_mst=mst[:(k-len(T))]
    return tree_weight(G,T+remainder_mst) 
    
