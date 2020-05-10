import random
import numpy as np 
import operator
import pandas as pd
import matplotlib.pyplot as plt 


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

# This will return random routes with size of cityList
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# This will return list of random individual(routes) of size popSize with each route has size of len(cityList)
def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

# This will return results of population's fitness in sorted order
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

# This will select individuals(routes) for mating
def selection(popRanked, eliteSize):
    selectionResults = []

    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])

    # finding cumulative sum of fitness column
    df['cum_sum'] = df.Fitness.cumsum()

    # finding cumulative percentage of cumulative sum
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    # selection is reserved for eliteSize because they are fittest
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])

    # selection of rest of the individuals on the basis of roulette wheel
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

# This will return the individual for breeding
def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

# create an offspring from parents
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    # randomly selecting two indexes for crossover
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # applying crossover
    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

# this will return the children by mating individuals in matingpool
def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize

    # shuffling the matingpool
    pool = random.sample(matingpool, len(matingpool))

    # preserving best individuals from the matingpool
    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    # creating children by breeding rest of the individuals
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

# this function mutates an individual with probability of mutationRate(swapped mutation)
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# this function returns mutated population(next generation)
def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

# This function will give next generation(routes)
def nextGeneration(currentGen, eliteSize, mutationRate):
    # sorted rank of individual(route) in a population
    popRanked = rankRoutes(currentGen)

    # selected individuals for mating
    selectionResults = selection(popRanked, eliteSize)

    # the list of individuals for breeding
    matingpool = matingPool(currentGen, selectionResults)

    # the list of children after breeding
    children = breedPopulation(matingpool, eliteSize)

    # the list of next generation population
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    #this gives initial population
    pop = initialPopulation(popSize, population)

    # Distance of intial population's best individual(best route)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    # Running for generations for finding optimum route(population)
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    # Distance of final population's best individual(best route)
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))

    # returning best route(individual)
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute


cityList = []

# This will create a list of city co-ordinates with size 25
for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

# Here, popSize = No. of routes, eliteSize is how many top fit individual to choose
# generations = no. of iterations
print(geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500))
