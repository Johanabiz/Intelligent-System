import random as r

class GA:

    def __init__(self, populationSize, crossoverP, mutationP, nGenerations):
        self.populationSize = populationSize
        self.crossoverP = crossoverP
        self.mutationP = mutationP
        self.nGenerations = nGenerations
        self.evolution = []
    
    def run(self):
        # intialize
        self.population = self._generate()
        self.best = self._bestEntity()
        self.evolution.append( self.best.getFitness() )
        # run until termination (number of generations as defined)
        time = 0
        print('Best performance in initial generation')
        self.best.display()
        while time < self.nGenerations :
            self._algo()
            time += 1
            # print best option in current generation
            self.best = self._bestEntity()
            self.evolution.append( self.best.getFitness() )
            if time == self.nGenerations-1 :
                print('Best performance in generation ' + str(time))
                self.best.display()

    # algorithm (based on slide 5)
    def _algo(self):
        
        # create mating pool
        matingPool = self._select()
        #matingPool = []
        #while len(matingPool) != len(self.population) :
            # entity = self._select()
            # matingPool.append(entity)
                    
        # generate new population from the mating pool
        self.population = []
        while len(matingPool) != 0 : 
            # randomly choose and remove two
            p1 = r.choice(matingPool)
            matingPool.remove(p1)
            p2 = r.choice(matingPool)
            matingPool.remove(p2)
            # do crossover with probability P
            x = r.random()
            if x < self.crossoverP :
                [c1, c2] = self._crossover(p1,p2)
            else :
                c1, c2 = p1, p2
            # do mutation with probability P (for each child and each of his genes)
            for child in [c1,c2] :
                genes = child.getGenes() #
                genesToMutateList = [] #
                for gNumber in range(len(genes)) : 
                    x = r.random()
                    if x < self.mutationP :
                        genesToMutateList.append(gNumber) #
                        self._mutation(child, genesToMutateList)
                self.population.append(child)
    
    # generation
    def _generate(self):
        # to be implemented 
        print('Please implement')
               
    # fitness - selection        
    def _select(self):
        # to be implemented 
        print('Please implement')
    
    # reproduction - crossover    
    def _crossover(self, p1, p2):
        # to be implemented 
        print('Please implement')
    
    # mutation
    def _mutation(self, child, genesToMutateList):
        # to be implemented 
        print('Please implement')
    
    def _bestEntity(self) :
        # to be implemented 
        print('Please implement')
            
            