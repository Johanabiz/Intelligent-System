from Entity import Entity
import random as r

class Path(Entity):

    def __init__(self, genes, matrix):
        self.matrix = matrix
        Entity.__init__(self, genes)
    
    def _calculateFitness(self):
        fit = 0
        for i in range(len(self.genes)-1):
            currentC = self.genes[i]
            nextC = self.genes[i+1]
            fit += self.matrix[currentC.getIndex()][nextC.getIndex()]
        # back to the origin (starting point)
        fit += self.matrix[nextC.getIndex()][self.genes[0].getIndex()]
        return fit
        
    def display(self):
        print('Fitness: ' + str(self.fitness))
        print('Path:')
        index = 1
        for g in self.genes:
            print('City ' + str(g.getIndex()))
            index += 1
        print()
    
    def mutateGene(self, geneIndexList):
        if len(geneIndexList) > 1 :
            shuffledList = []
            for el in geneIndexList:
                shuffledList.append(self.genes[el])
            r.shuffle(shuffledList)
            for i, el in enumerate(geneIndexList):
                self.genes[el] = shuffledList[i]
            self.fitness = self._calculateFitness()
            '''
            for i in range(len(shuffledList)):
                temp = self.genes[geneIndexList[i]]
                self.genes[geneIndexList[i]] = self.genes[shuffledList[i]]
                self.genes[shuffledList[i]] = temp
            '''
        #else:
            #print('Not enough genes to mutate')
            #print()
    
    def copy(self):
        return Path(self.genes, self.matrix)
