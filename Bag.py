import random as r
from Entity import Entity

class Bag(Entity):

    def __init__(self, genes, limit):
        Entity.__init__(self, genes)
        self.limit = limit
        self.totalWeight = self._calculateWeight()
    
    def _calculateFitness(self):
        fit = 0
        for g in self.genes:
            if g.getActive():
                fit += g.getValue()
        return fit
    
    def _calculateWeight(self):
        total = 0
        for g in self.genes:
            if g.getActive():
                total += g.getWeight()
        return total
        
    def display(self):
        print('Fitness: ' + str(self.fitness))
        print('Bag weight: ' + str(self.totalWeight))
        for i, g in enumerate(self.genes):
            if g.getActive():
                print('Item ' + str(g.getValue()) + ': yes, ' + str(g.getWeight()) + ' weight')
            else: 
                print('Item ' + str(g.getValue()) + ': no')
        print()
    
    def mutateGene(self, geneIndexList):
        while geneIndexList != [] :
            i = r.choice(geneIndexList)
            geneIndexList.remove(i)
            g = self.genes[i]
            if (g.getActive()) or (self.totalWeight + g.getWeight() <= self.limit):
                g.mutate()
                self.totalWeight = self._calculateWeight()
                self.fitness = self._calculateFitness() 
                
    def copy(self):
        genes = []
        for g in self.genes:
            genes.append(g.copy())
        c = Bag(genes, self.limit)
        return c

'''
class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
'''