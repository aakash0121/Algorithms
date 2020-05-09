from ypstruct import structure
import numpy as np 

def crossover(p1, p2, gamma = 0.1):
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    alpha = np.random.uniform(gamma, 1 + gamma, *c1.position.shape)
    c1.position = alpha*p1.position + (1-gamma)*p2.position
    c2.position = alpha*p2.position + (1-gamma)*p1.position

    return c1, c2

def run(problem, params):
    
    # Problem Information
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax

    # Parameters
    maxit = params.maxit
    npop = params.npop
    pc = params.pc
    nc = np.round(pc*npop/2)*2


    # empty individual template
    empty_individual = structure()
    empty_individual.position = None
    empty_individual.cost = None

    # Best solution ever found
    bestsol = empty_individual.deepcopy()
    bestsol.cost = np.inf


    # Initialize Population
    pop = empty_individual.repeat(npop)
    for i in range(npop):
        pop[i].position = np.random.uniform(varmin, varmax, nvar)
        pop[i].cost = costfunc(pop[i].position)
        if pop[i] < bestsol.cost:
            bestsol = pop[i].deepcopy()
    
    # Best cost of iterations
    bestcost = np.empty(maxit)

    # Main loop
    for it in range(maxit):
        popc = []
        for k in range(nc//2):
            #select parents randomly
            q = np.random.permutation(npop)
            p1 = pop[q[0]]
            p2 = pop[q[1]]

            # performing crossover
            c1, c2 = crossover(p1, p2)


    
    # Output
    out = structure()
    out.pop = pop
    return out
