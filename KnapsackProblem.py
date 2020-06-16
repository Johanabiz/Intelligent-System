import random as r
from itertools import accumulate
from Bag import Bag
from Item import Item
from GA import GA

# KNAPSACK PROBLEM
# Here the knapsack is an entity, and each item inside is a gene
class KnapsackProblem(GA):

    def __init__(self, populationSize, crossoverP, mutationP, nGenerations, 
                 possibleItems, limit):     
        GA.__init__(self, populationSize, crossoverP, mutationP, nGenerations)
        self.limit = limit
        self.items = possibleItems
        self.nItems = len(possibleItems)
        
    # Generation (of initial population)
    def _generate(self):
        self.knapsacks = self._randomPoulation()
        return self.knapsacks
    
    # Generating population of knapsacks
    def _randomPoulation(self):
        knapsacks = []
        for k in range(self.populationSize):
            genom = [0]*self.nItems
            indexList = list(range(self.nItems))
            total = 0
            
            for i in range(self.nItems):
                # Choose item by index
                x = r.choice(indexList)
                indexList.remove(x)
                item = self.items[x]
                a = r.choice([True,False])
                if total + item.getWeight() > self.limit :
                    a = False
                elif a:
                    total += item.getWeight()
                gene =  Item(weight=item.getWeight(), value=item.getValue(), active=a)
                genom[x] = gene
            e = Bag(genes = genom, limit = self.limit)
            knapsacks.append(e)
        return knapsacks
    
    # fitness - selection
    def _select(self): 
        # rollete probabilities
        results = []
        for p in self.population:
            results.append(p.getFitness())
        total = sum(results)
        prob = []
        for i in range(len(self.population)):
            prob.append( results[i]/total )
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
            
        '''
        x = r.random()
        if x < self.elitismP :
            best = self._bestEntity()
        else :
            best = r.choice(self.population)
        return best
        '''
        
    # reproduction - crossover    
    def _crossover(self, p1, p2):
        crossoverType = self.nItems # uniform cross over
        c = []
        for i in range(2):
            genes = []
            for i in range(crossoverType) :
                x = r.choice([p1,p2])
                g = x.getGenes()
                genes.append(g[i])
            child = Bag(genes = genes, limit = self.limit)
            # Check legality, otherwise retun random parent
            if child.totalWeight < self.limit: 
                c.append(child)
                #print('yay')
            else: 
                c.append(x)
                #print('fail')
        return c
    
    # mutation
    def _mutation(self, child, genesToMutateList):
        # mutate as long as legal
        child.mutateGene(genesToMutateList)
    
    # Best (selection)
    def _bestEntity(self) :
        best = self.population[0]
        value = best.getFitness()
        for i in range(1,len(self.population)):
            if self.population[i].getFitness() > value :
                best = self.population[i]
                value = self.population[i].getFitness()
        return best
        
# Test

# parameters
populationSize=10
nGenerations = 50
cP = 0.6
mP = 0.6

nItems=50
limit=20

# Generating all possible items
def possibleGenes(nItems):
    items = []
    for i in range(nItems):
        w = r.randint(1,10)
        x = Item(weight=w, value=i+1, active=False)
        items.append(x)
    notOrdered = items.copy()
    r.shuffle(notOrdered)
    return items, notOrdered

# Run
'''
ordered, shuffled = possibleGenes(nItems)

kp = KnapsackProblem(populationSize=populationSize, crossoverP=cP, mutationP=mP, 
                     nGenerations=nGenerations, possibleItems = ordered, limit=limit)
kp.run()

Xv = []
for v in kp.evolution:
    Xv.append( v )

import matplotlib.pyplot as plt
plt.plot(Xv)

check = kp.items
solution = kp.best
'''

# Simulate

n = 100
resultsOrdered, resultsShuffeled = [], []

for i in range(n):
    ordered, shuffled = possibleGenes(nItems)
    
    kp1 = KnapsackProblem(populationSize=populationSize, crossoverP=cP, mutationP=mP, 
                     nGenerations=nGenerations, possibleItems = ordered, limit=limit)
    kp1.run()
    resultsOrdered.append(kp1.evolution)
    
    kp2 = KnapsackProblem(populationSize=populationSize, crossoverP=cP, mutationP=mP, 
                     nGenerations=nGenerations, possibleItems = shuffled, limit=limit)
    kp2.run()
    resultsShuffeled.append(kp2.evolution)

# Vsualize
Xordered = [0] * (nGenerations)
Xshuffled = [0] * (nGenerations)
for s in range(n):
    for g in range(nGenerations):
        Xordered[g] += resultsOrdered[s][g]
        Xshuffled[g] += resultsShuffeled[s][g]
        
Xordered = [el / n for el in Xordered]
Xshuffled = [el / n for el in Xshuffled]

import matplotlib.pyplot as plt
plt.plot(Xordered, label='Ordered')
plt.plot(Xshuffled, label='Random shuffle')
plt.legend()
plt.title('Knapsack solution (p=' + str(cP) + ')')
plt.xlabel('Generation')
plt.ylabel('Fittest bag value (avg.)')
plt.show()
