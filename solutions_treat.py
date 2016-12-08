solutions=[]
solution_weight=float("inf")

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
