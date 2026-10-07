import math
import random
import timeit

intDiv = 0

##Worst Case should be O(log2(n)) or O(lgn)
def primeFactorization(n):
    global intDiv
    arr = []
    ##adds all multiples of 2 from n into an array
    while n % 2 == 0:
        arr.append(2)
        n //= 2
        intDiv += 2
    
    ##finds all prime factors from 3 to the the square root of n
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            arr.append(i)
            n //= i
            intDiv += 2
    ##if n is greater than 2, it adds that prime factor to the array
    if n > 2:
        arr.append(n)
    return arr
    ##end of primeFactorization(n)

##Worst Case should be O(m*n) in the local scope, or O(lgm*lgn) in the scope of the entire algorithm
def commonFactors(m,n):
    ret = 1
    for i in range(len(m)):
        j = 0
        while j < len(n):
            if(m[i] == n[j]):
                ret *= n.pop(j)
                j = len(n)
            j += 1
        
    return ret
    #end of commondFactors(m,n)

def getInput():
    m = int(input("Welcome to Prime Factorization!\nPlease enter your two numbers.\nNum 1: "))
    n = int(input("Num 2: "))
    return m, n

def start(m, n):
    m = primeFactorization(m)
    n = primeFactorization(n)
    ##print(m)
    ##print(n)
    print("The GCD is:",commonFactors(m,n))

if __name__ == '__main__':
    ##m, n = getInput()
    ##m = random.randint(100,200)
    ##n = random.randint(50,99)
    print(timeit.timeit('m = random.randint(100,200); n = random.randint(50,99); start(m,n)', number=5, globals=globals()))
    print("Integer Divisions:", intDiv)
