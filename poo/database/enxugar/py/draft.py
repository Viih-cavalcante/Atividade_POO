class towel:
    def __init__(self, color :str, size :str) :
        self.color = color
        self.size = size
        self.Wetness :int = 0 

    def getMaxWetness(self) -> int :
        if self.size == "P" :
            return 10
        if self.size == "M" :
            return 20
        if self.size == "G":
            return 30
        return 0
    def dry(self, amount :int) -> None :
        self.Wetness += amount
        if  self.Wetness > self.getMaxWetness():
            print("Toalha enxarcada")
            self.wetness = self.getMaxWetness()
    


  