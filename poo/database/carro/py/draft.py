class Carro: 
    def __init__(self):
        self.passengers = 0
        self.passMax = 2
        self.gas = 0
        self.km = 0

    def __str__(self) -> str:
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    
def main ():
        carro = Carro()
        while True:
            line : str = input()
            print("$" + line)
            if line == "show":
                print(carro)
            elif line == "end":
                break
main ()