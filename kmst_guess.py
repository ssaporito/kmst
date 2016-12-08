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
    for v in G[u]:
        r+=G[u][v]['weight']
        if l>1:
            r+=P(G,v,l-1)
    P_memo[u][l]=r*l
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
    print(sol.edges())
    return sol
    

def kmst(G,k):
    T=[]
    search_level=3
    for v in G.nodes():
        P(G,v,search_level)
    #print(P_memo)
    P_sorted_v=list(map(lambda x:x[0],sorted(P_memo.items(),key=lambda x:x[1][search_level])))    
    print(P_sorted_v)
    return nx.minimum_spanning_tree(first_viable_solution2(G,P_sorted_v,k)).edges()
    #sorted(,key=lambda el:el[1])
    #kmst_backtrack(k+1,T,V,E)

solutions=[]

def test_kmst():
    global solutions
    G=nx.Graph()
    #e=[(0,1,3.0),(1,2,1.0),(0,2,2.0),(0,3,1.0),(3,1,0.5),(1,4,5.0),(2,4,3.0)]
    #e=[(0,1,1),(0,2,1),(0,3,2),(1,2,10),(2,3,1),(3,1,10),(2,4,1),(3,5,1),(6,2,2),(3,7,1)]
    e=[(0,1,1),(0,2,1),(1,3,10),(2,3,10),(3,4,2),(3,5,2),(4,6,3),(5,6,2)]
    G.add_weighted_edges_from(e)
    solution=kmst(G,4)    
    #print_solutions(G,get_weighted_solutions(G,solutions))
    try:
        min_solution=minimum_solution(get_weighted_solutions(G,[solution]))
        print(min_solution)
        selected=min_solution[0]
        #print(selected)
        pos=nx.spring_layout(G)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G,pos,edge_color='b')
        nx.draw_networkx_edges(G,pos,edgelist=selected,edge_color='r')
        nx.draw_networkx_labels(G,pos)
        #nx.draw_networkx_edge_labels(G,pos)
        plt.show()
        #print(sorted(solutions,key=lambda el:el[1])) #print asc sorted solutions
    except(TypeError,IndexError):
        print("Algum erro ocorreu ou não há solução armazenada.")

test_kmst()
    
    
