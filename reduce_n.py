import random
import timeit

intDiv = 0

##Best case is O(1), since min(m,n) is also the GCD, while the Worst case is O(min(m,n)-1).
def consecInt(m,n):
    global intDiv
    t = min(m,n)
    ##at most, this while loop runs min(m,n)-1 times
    while t > 0:
        if m % t == 0: ## not using 'and' as to track integer divisions
            if n % t == 0:
                print("GCD is:", t)
                intDiv += 2
                return t
            else:
                intDiv += 2
                t -= 1
        else:
            intDiv += 1
            t -= 1

def getInput():
    m = int(input("Num 1:"))
    n = int(input("Num 2:"))
    return m, n

def start(m,n):
    consecInt(m,n)

if __name__ == '__main__':
    ##m, n = getInput()
    print("\nReduce_N")
    ##keeping this at 10^6
    print(timeit.timeit('m = random.randint(1000000,2000000); n = random.randint(500000,999999); start(m,n)', number=5, globals=globals()))
    print("Integer Divisions:", intDiv)
