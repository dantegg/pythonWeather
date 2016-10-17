import string
import sys
from classB import classB

class classA:
    def __init__(self):
        self.slogen = 'hello,python'

    def printSolgen(self):
        print self.slogen
def main():
    AAA = classA()
    AAA.printSolgen()
    BBB = classB()
    BBB.printClassB()

if __name__ == '__main__':
    main()
