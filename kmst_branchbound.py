import networkx as nx
import matplotlib.pyplot as plt
from solutions_treat import *

solutions=[-1]

def kmst_branchbound(G,k,T,V,E):
    if is_viable(k,T,V):        
        if is_solution(k,T):
            choose_best_solution(G,T)
        else:
            
            for i in range(0,len(E)):
                if not V or E[i][0] in V or E[i][1] in V:
                    T2=list(T)
                    E2=list(E)
                    V2=dict(V)
                    V2[E[i][0]]=True
                    V2[E[i][1]]=True
                    T2.append(E2.pop(i))            
                    kmst_branchbound(G,k-1,T2,V2,E2)

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
    if T==-1:        
        return float("inf")
    else:
        for t in T:
            r+=G[t[0]][t[1]]['weight']
        return r

def choose_best_solution(G,s2):
    global solutions
    weight1=tree_weight(G,solutions[0])
    weight2=tree_weight(G,s2)
    if weight1>weight2:
        solutions=[s2]
    elif weight1==weight2:
        solutions.append(s2)    

def lower_bound(G,k,T,V,E):
    return 1

def upper_bound(G,k,T,V,E):
    return 10
    
def kmst(G,k):
    T=[]
    V=dict([])
    E=G.edges()
    kmst_branchbound(G,k+1,T,V,E)    

def test_kmst():
    G=nx.Graph()
    #e=[(0,1,3.0),(1,2,1.0),(0,2,2.0),(0,3,1.0),(3,1,0.5),(1,4,5.0),(2,4,3.0)]
    #e=[(0,1,1),(0,2,1),(0,3,2),(1,2,10),(2,3,1),(3,1,10),(2,4,1),(3,5,1),(6,2,2),(3,7,1)]
    e=[(0,1,1),(0,2,1),(1,3,10),(2,3,10),(3,4,2),(3,5,2),(4,6,3),(5,6,2)]
    G.add_weighted_edges_from(e)
    kmst(G,3)
    global solutions
    #print_solutions(G,get_weighted_solutions(G,solutions))
    try:                
        min_solution=minimum_solution(get_weighted_solutions(G,solutions))
        print(min_solution)
        selected=min_solution[0]
        pos=nx.spring_layout(G)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G,pos,edge_color='b')
        nx.draw_networkx_edges(G,pos,edgelist=selected,edge_color='r')
        nx.draw_networkx_labels(G,pos)
        #nx.draw_networkx_edge_labels(G,pos)
        plt.show()
        #print(sorted(solutions,key=lambda el:el[1])) #print asc sorted solutions
    except(TypeError,IndexError):
        print("Algum erro ocorreu ou não há solução.")

test_kmst()
    
    
