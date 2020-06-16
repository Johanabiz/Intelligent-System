import random as r
import pandas as pd
from itertools import accumulate
import math as m
from City import City
from Path import Path
from GA import GA
from CX2 import CX2

# SALESMAN PROBLEM
# Here the path is the entity, and the order of each city is a gene
class SalesmanProblem(GA):

    def __init__(self, populationSize, crossoverP, mutationP, nGenerations, nCities):     
        GA.__init__(self, populationSize, crossoverP, mutationP, nGenerations)
        self.nCities = nCities

    # Generation (of initial population)
    def _generate(self):
        self.cities = self._possibleGenes()
        self.matrix = self._distanceMatrix()
        self.travels = self._randomPoulation()
        return self.travels
    
    # Generating all cities
    def _possibleGenes(self):
        cities = []
        for i in range(self.nCities):
            l = r.randint(0,360)
            x = City(index=i, location=l)
            cities.append(x)
        return cities
    
    # Generating population of travels
    def _randomPoulation(self):
        travels = []
        for t in range(self.populationSize):
            order_genom = []
            optionalCities = list(range(self.nCities))
            for c in range(self.nCities):
                x = r.choice(optionalCities)
                optionalCities.remove(x)
                order_genom.append(self.cities[x])
            e = Path(order_genom, self.matrix)
            travels.append(e) 
            # e.display()             
        return travels 
    
    # distances
    def _distanceMatrix(self):
        matrix = []
        for i in range(self.nCities):
            cDistances = []
            for j in range(self.nCities):
                cDistances.append(self._distance(self.cities[i],self.cities[j]))
            matrix.append(cDistances)
        return matrix
        
    def _distance(self, c1, c2):
        l1 = c1.getLocation()
        l2 = c2.getLocation()
        angle = min(m.fabs(l1-l2), m.fabs(l1-l2-360))
        d = m.sqrt( 2 - 2 * m.cos(angle) )
        return d
    
    # selection
    def _select(self): 
        # rollete probabilities
        results = []
        for p in self.population:
            results.append(p.getFitness())
        total = sum(results)
        prob = []
        for i in range(len(self.population)):
            prob.append( 1 - (results[i]/total) )
        self.accumProb = list(accumulate(prob))
        # select by the pobabilities
        matingPool = []
        while len(matingPool) != len(self.population) :
            x = r.random()
            i = 0
            found = False
            while (i < len(self.accumProb)) and (not found):        
                if x < self.accumProb[i]:
                    found = True
                else: 
                    i += 1
            entity = self.population[i].copy()
            matingPool.append(entity)
        return matingPool
    
    # reproduction - crossover 
    # Cycle Croessover 2 (CX2) - (Hussain et al., 2017)
    def _crossover(self, p1, p2):
        g1, g2 = [], []
        for i in range(self.nCities): 
            g1.append(p1.getGenes()[i].getIndex())
            g2.append(p2.getGenes()[i].getIndex())
        c1, c2 = CX2(g1,g2).getResult()
        
        genesC1, genesC2 = [], []
        for i in range(self.nCities):
            genesC1.append(self.cities[c1[i]]) 
            genesC2.append(self.cities[c2[i]])
        c1 = Path(genesC1, self.matrix)
        c2 = Path(genesC2, self.matrix)
        return c1, c2
    
    # mutation
    def _mutation(self, child, genesToMutateList):
        child.mutateGene(genesToMutateList)  

    # Best (selection)
    def _bestEntity(self) :
        best = self.population[0]
        value = best.getFitness()
        for i in range(1,len(self.population)):
            if self.population[i].getFitness() < value :
                best = self.population[i]
                value = self.population[i].getFitness()
        return best
    
# Test
        
# parameters
populationSize=10
nGenerations = 50
cP = 0.6
mP = 0.6

nCities=6

# Run
'''
sp = SalesmanProblem(populationSize=populationSize, crossoverP=cP, mutationP=mP, 
                     nGenerations=nGenerations, nCities=nCities)
sp.run()

Xv = []
for v in sp.evolution:
    Xv.append( v )

import matplotlib.pyplot as plt
plt.plot(Xv)

check = pd.DataFrame(sp.matrix)
solution = sp.best
'''

# Simulate
n = 100
results = []

for i in range(n):
    sp = SalesmanProblem(populationSize=populationSize, crossoverP=cP, mutationP=mP, 
                         nGenerations=nGenerations, nCities=nCities)
    sp.run()
    results.append(sp.evolution)

X = [0] * (nGenerations)
for s in range(n):
    for g in range(nGenerations):
        X[g] += results[s][g]

import matplotlib.pyplot as plt
plt.plot(X)
plt.title('Salesman solution (p=' + str(cP) + ')')
plt.xlabel('Generation')
plt.ylabel('Shortest path (avg.)')
plt.show()
   
