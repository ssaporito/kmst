from kmst_guess import *
from kmst_branchbound import *
import time
import random

def test_kmst(n_nodes,k,tries,draw):
    solutions=[]
    solution_weight=float("inf")
    G=nx.Graph()
    #e=[(0,1,3.0),(1,2,1.0),(0,2,2.0),(0,3,1.0),(3,1,0.5),(1,4,5.0),(2,4,3.0)]
    #e=[(0,1,1),(0,2,1),(0,3,2),(1,2,10),(2,3,1),(3,1,10),(2,4,1),(3,5,1),(6,2,2),(3,7,1)]
    #e=[(0,1,1),(0,2,1),(1,3,10),(2,3,10),(3,4,2),(3,5,2),(4,6,3),(5,6,2)]
    #G.add_weighted_edges_from(e)
    G=nx.complete_graph(n_nodes)
    i=1    
    for e in G.edges():
    #    G[e[0]][e[1]]['weight']=i
        G[e[0]][e[1]]['weight']=random.uniform(1,100)
        i+=1
    n=G.number_of_nodes()
    m=G.number_of_edges()
    #tries=10
    print("n="+str(n)+",k="+str(k)+",m="+str(m))

    T=[]
    V=dict([])
    E=G.edges()    
    start=time.time()    
    for i in range(0,tries):
        #pass
        #global solutions
        solutions.clear()
        global P_memo
        P_memo.clear()
        kmst_guess(G,k,solutions)    
    end=time.time()
    print("Heuristics")
    print_results(solutions,start,end,tries,G)
    val_guess=minimum_solution(get_weighted_solutions(G,solutions))[1]
    
    T=[]
    V=dict([])
    E=G.edges()    
    start=time.time()    
    for i in range(0,tries):        
        solutions.clear()
        kmst_branchbound(G,k,T,V,E,solutions,[solution_weight])
    end=time.time()
    print("Branch and Bound")
    print_results(solutions,start,end,tries,G)
    val_branch=minimum_solution(get_weighted_solutions(G,solutions))[1]

    print("Diff: "+str((val_guess-val_branch)/(val_branch)))
    
    
    
    #print_solutions(G,get_weighted_solutions(G,solutions))
    try:
        #print(solutions)        
        min_solution=minimum_solution(get_weighted_solutions(G,solutions))
        #print(min_solution)
        #print(solution_weight)
        if draw:
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
        print("An error occurred or there is no solution.")
    
    
test_kmst(8,5,1,False)
