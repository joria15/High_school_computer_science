class SimpleCalculator:
    """
    A simple calculator that has the functions of 
    additioning/subtracting/dviding/multiplying/square root/exponent/percentage/paranthesees to floats and integers
    while following 'PEDMAS'


    Attributes:
        _equation: (str) (private)
    
    Return:

    >>> 
    """
    def __init__(self, equation: str) -> None:
        self._equation = equation
        self._history = []

    def __str__(self) -> str:
        return f"Equation: [{self._equation}]"
    
    def menu(self) -> None:
        pass

    def get_equation(self) -> str:
        return self._equation
    #use this to show what your previous was and also append to a list for history

    def calculate(self) -> None:
        equation = self.get_equation
        #quick input calculation
        #use try to see if it is division by zero or other errors
        pass
    
    def get_history(self) -> None:
        spot_history = 1

        for equation in self._history:
            print(f"{spot_history}. [ {equation} ]")
            spot_history += 1

    def test_calculate(self, equation: str) -> bool:
        #use try to see if it is division by zero or other errors
        pass

    def new_calculation(self) -> None:
        #use try to see if it is division by zero or other errors and for yes no
        while True:
            new_equation = str(input("Would you like to input a new calcuation (y/n): "))
            
            if new_equation.lower() != "y" or new_equation.lower() != "n":
                print("Input 'y' = (yes) for a new calculation or 'n' = (no) to stop")
            break

        if new_equation.lower() == "n":
            return None
        
        elif new_equation.lower() == "y":
            while True:
                equation = str(input("Equation: "))
                if self.test_calculate(equation) == True:
                    self._history()
                    #same process as calculate
                    #self._history.append((equation, answer))
                    break

                elif self.test_calculate(equation) == False:
                    print("Invalid, try again")
        
        self.menu() # go back to the menu to pick between history or new calculation
        
                    
        

def main():
    #make a quick claculation, so basically if you want to quick calculate, manually see history and calculate or polymorphism
    #then create objects here, but if you want menu for interactive history and new calculation, then put menu function
    #basically, quick calcluate is for calculate function and get history/and get equation and __str__ method
    # /normal is the menu function which gets new equation or get history
    eq = SimpleCalculator("12 + 5")
    print(eq)

if __name__ == "__main__":
    main()