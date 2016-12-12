import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *
from math import exp

P_memo=dict([])

def P(G,u,l):
    global P_memo
    if u in P_memo:
        if l in P_memo[u]:
            return P_memo[u][l]
    else:
        P_memo[u]=dict([])
    r=1/v_value(G,u)
    if l==0:
        pass
    else:
        for v in G[u]:                                
            r*=P(G,v,l-1)*dec_func(G[u][v]['weight'])
        r*=dec_func(l)
    P_memo[u][l]=r
    return P_memo[u][l]

def dec_func(x):
    return exp(-x)

def inc_func(x):
    return x

def v_value(G,u):
    w_list=[]
    for v in G[u]:
        w_list.append(G[u][v]['weight'])        
    sorted_w_list=sorted(w_list)
    r=0
    for i in range(0,len(sorted_w_list)):
        r+=inc_func(i+1)*sorted_w_list[i]
    r/=(len(sorted_w_list))*(len(sorted_w_list)+1)/2
    return r
    
def first_viable_solution(G,V,k):
    u=V[0]
    v_list=[u]
    V.remove(u)
    V_removal=[]
    while True:
        for v in V:
            for t in v_list: 
                if v in G[t] and v not in v_list:
                    v_list+=[v]
                    V_removal+=[v]
                    if len(v_list)==k:                        
                        sol=G.subgraph(v_list)                        
                        return sol
        for v in V_removal:
            if v in V:
                V.remove(v)            
        V_removal=[]    
    

def kmst_guess(G,k,solutions):
    if k>G.number_of_nodes():
        print("k must be lower than |V|")
        return False
    search_level=k
    for v in G.nodes():
        P(G,v,search_level)
    #print(P_memo)
    sorted_list=sorted(P_memo.items(),key=lambda x:x[1][search_level],reverse=True)    
    P_sorted_v=list(map(lambda x:x[0],sorted_list))
    #print(sorted_list)
    solutions.append(nx.minimum_spanning_tree(first_viable_solution(G,P_sorted_v,k)).edges())
    #print(solutions)
    #sorted(,key=lambda el:el[1])
    #kmst_backtrack(k+1,T,V,E)
    
    
