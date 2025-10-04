class Towel:
    def __init__(self, color :str, size :str):
        self.color = color
        self.size = size
        self.wetness :int = 0
    
    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size =="G":
            return 30
        return 0
    
    def enxugar(self, amount :int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
        
    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
       return self.wetness == 0
    
    def mostrar(self) -> None :
        print(self)

    def __str__(self) -> str:
        return f"Cor: {self.color }, Tamanho: {self.size }, Umidade: {self.wetness}"

def main():
    toalha = Towel("azul" , "P")
while True:
    line : str = input()
    print("$" + line)
    args :list [str] = line.split()
    if args[0] == "end" :
      break
    elif args[0] == "criar" :
        color = args[1]
        size = args[2]
        toalha = Towel(color , size)
    elif args[0] == "mostrar":
        print(toalha)
    elif args[0] == "enxugar":
        amount = int(args[1])
        toalha.enxugar(amount)
    elif args[0] == "seca":
        print("sim" if toalha.isDry() else "nao")
    elif args [0] == "torcer":
        toalha.wringOut()
main()


        