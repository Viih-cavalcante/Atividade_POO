class Animal:
    def __init__(self,species :str, sound :str):
        self.species  = species
        self.age : int = 0
        self.sound = sound
    
    def makeSound (self) -> str:
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        else:
            return self.sound
    
    def ageBy(self,increment: int) -> None:
        if self.age >= 4:
            print(f"warning: {self.species} morreu.")
            return


    
    




        
    