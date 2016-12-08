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

def kmst(G,k):
    T=[]
    search_level=3
    for v in G.nodes():
        P(G,v,search_level)
    #print(P_memo)
    P_sorted_v=list(map(lambda x:x[0],sorted(P_memo.items(),key=lambda x:x[1][search_level])))
    count_v=0
    sub=nx.Graph()
    print(P_sorted_v)
    # gotta fix this
    while True:
        sub=G.subgraph(P_sorted_v) 
        if nx.is_connected(sub):
            print(nx.minimum_spanning_tree(sub))
            break    
    return nx.minimum_spanning_tree(sub)
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
    solution=kmst(G,3)    
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
    
    
