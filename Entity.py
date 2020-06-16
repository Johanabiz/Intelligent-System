class Entity:

    def __init__(self, genes):
        self.genes = genes
        self.fitness = self._calculateFitness()  # check it always possible !!!!
    
    def _calculateFitness(self):
        # to be implemented 
        print('Please implement')
    
    def display(self):
        # to be implemented 
        print('Please implement')
    
    def mutateGene(self, geneIndexList):
        # to be implemented 
        print('Please implement')
    
    def getGenes(self):
        return self.genes

    def getFitness(self):
        return self.fitness
    

        

     
'''
class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
'''