import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *


P_memo=dict([])

def P(G,u,l):
    global P_memo
    if u in P_memo:
        if l in P_memo[u]:
            return P_memo[u][l]
    else:
        P_memo[u]=dict([])
    r=0
    if l==0:
        r=0
    else:
        for v in G[u]:        
            if l>0:
                r+=G[u][v]['weight']*l
                r+=P(G,v,l-1)        
    P_memo[u][l]=r
    return P_memo[u][l]

def first_viable_solution(G,V,k):
    start_i=0
    sol=[V[start_i]]
    candidate_i=start_i+1
    print(V)
    while len(sol)<k+1:
        if candidate_i==len(V):            
            start_i+=1
            candidate_i=start_i+1            
            sol=[V[start_i]]
        candidate=V[candidate_i]
        new_sol=sol+[candidate]
        sub=G.subgraph(new_sol) 
        if nx.is_connected(sub):
            sol=new_sol
            print(sol)                        
        candidate_i+=1        
    return sol

def first_viable_solution2(G,V,k):
    u=V[0]
    v_list=[u]
    V.remove(u)
    V_removal=[]
    while len(v_list)<k+1:
        for v in V:
            for t in v_list: 
                if v in G[t] and v not in v_list:
                  v_list+=[v]
                  V_removal+=[v]        
        for v in V_removal:
            V.remove(v)        
        V_removal=[]    
    sol=G.subgraph(v_list)
    #print(sol.edges())
    return sol
    

def kmst_guess(G,k):
    global solutions
    search_level=3
    for v in G.nodes():
        P(G,v,search_level)
    #print(P_memo)
    P_sorted_v=list(map(lambda x:x[0],sorted(P_memo.items(),key=lambda x:x[1][search_level])))    
    #print(P_sorted_v)
    solutions.append(nx.minimum_spanning_tree(first_viable_solution2(G,P_sorted_v,k)).edges())
    #sorted(,key=lambda el:el[1])
    #kmst_backtrack(k+1,T,V,E)
    
    
