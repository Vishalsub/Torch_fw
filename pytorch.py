import os
import random
import math

class calculator():
    def __init__(self,num1, num2)->int:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2


def main():
    machine = calculator(20, 20)
    results = machine.add()
    print(results)

if __name__ == "__main__":
    main()
