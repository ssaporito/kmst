def get_weighted_solutions(G,solutions):
    weighted_solutions=[]
    for s in solutions:
        weighted_solutions.append([s])
        r=0
        for t in s:
           r+=G[t[0]][t[1]]['weight']
        weighted_solutions[-1].append(r)
    return weighted_solutions

def print_solutions(G,solutions):    
    print(sorted(solutions,key=lambda el:el[1])) #print asc sorted solutions
    
def minimum_solution(solutions):
    min_i=-1
    min_val=float("inf")
    
    for i in range(0,len(solutions)):
        if solutions[i][1]<min_val:
            min_val=solutions[i][1]
            min_i=i
    return solutions[min_i]

def print_results(solutions,start,end,tries,G):
    if len(solutions)>0:
        average_time=(end-start)*1000/tries
        min_solution=minimum_solution(get_weighted_solutions(G,solutions))    
        print("Time taken:"+str(average_time)+"ms")    
        print(solutions)    
        print("Min:"+str(min_solution[1]))        
    else:
        print("No solution found.")
