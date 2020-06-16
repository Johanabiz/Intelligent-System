# Cycle Croessover 2 (CX2)
# (Hussain et al., 2017)

class CX2():
    
    def __init__(self, g1, g2):
        self.result = self._crossover(g1,g2)
        
    def _crossover(self, g1, g2):
        
        # step 1
        n = len(g1)
        c1 = [-9]*n
        c2 = [-9]*n
        k = 0
        
        while (-9 in c2) :
            first = self._getFirstNotThere(c1,g2)
            i = first
            # step 2
            c1[k] = g2[i]
            while (g1[first] not in c2) :
                # step 3
                i = self._find(g2[i], g1)
                i = self._find(g2[i], g1)
                c2[k] = g2[i]
                # step 4
                i = self._find(g2[i], g1)
                if k+1 < len(c1) :
                    c1[k+1] = g2[i]    
                k += 1
            
        return c1,c2
        
    def _find(self, x, g):
        return g.index(x)
    
    def _getFirstNotThere(self, c, g):
        for i in range(len(g)):
            if g[i] not in c:
                return i
    
    def getResult(self):
        return self.result
 
#g1 = [3, 4, 8, 2, 7, 1, 6, 5]  
#g2 = [4, 2, 5, 1, 6, 8, 3, 7]        

#g1 = [1, 2, 3, 4, 5, 6, 7, 8] 
#g2 = [2, 7, 5, 8, 4, 1, 6, 3] 

#g1 = [1, 4, 5, 3, 0, 6, 2]
#g2 = [5, 0, 1, 3, 2, 6, 4]        
#c1, c2 = CX2(g1,g2).getResult()


