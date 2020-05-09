import numpy as np 
import matplotlib.pyplot as plt 
from ypstruct import structure
import ga

# sphere cost function
def sphere(x):
    return sum(map(lambda a:a**2, x))

# Problem definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA params
params = structure()
params.maxit = 1000
params.npop = 100
params.pc = 1
params.gamma = 0.1
params.mu = 0.1
params.sigma = 0.1

# Run GA
out = ga.run(problem, params)

# Results
