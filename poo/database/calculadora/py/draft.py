
class Calculadora:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def mostrar(self) -> None:
        print(self)

    def charge(self, increment: int) -> None:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float) -> None:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.display = a + b
        self.battery -= 1
    

    def div(self, a: float, b: float) -> None:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b
        self.battery -= 1


def main():
    calc = Calculadora(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calc = Calculadora(batteryMax)
        elif args[0] == "show":
            calc.mostrar()
        elif args[0] == "charge":
            increment = int(args[1])
            calc.charge(increment)
        elif args[0] == "sum":
            a = float(args[1])
            b = float(args[2])
            calc.sum(a, b)
        elif args[0] == "div":
            a = float(args[1])
            b = float(args[2])
            calc.div(a, b)


main()