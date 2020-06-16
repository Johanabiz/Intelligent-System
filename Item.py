class Item:

    def __init__(self, weight, value, active):
        self._weight = weight
        self._value = value
        self._active = active
    
    def getWeight(self):
        return self._weight
    
    def getValue(self):
        return self._value
    
    def getActive(self):
        return self._active
    
    def mutate(self):
        self._active = not self._active
    
    def copy(self):
        c = Item(self._weight, self._value, self._active)
        return c

        
