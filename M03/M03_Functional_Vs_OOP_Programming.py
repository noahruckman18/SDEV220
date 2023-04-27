"""
Programmer: Noah Ruckman
Title: M03_Functional_Vs_OOP_Programming.py
Summary: Uses OOP and Functional paradigms (subtract and division) and prints the results from the arguments entered. 
Version: 1.0
Last Revision: 4/8/2023
"""

def subtract(val1, val2):
    return val1-val2

def division(val1, val2):
    return val1/val2

class do_math():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
            
    def divide(self):
        return self.val1/self.val2
    
    def subtract(self):
        return self.val1-self.val2
        
        
print(subtract(10,5))
print(division(10,5))
calculate = do_math(20,10)
print(calculate.divide())
print(calculate.subtract())


                