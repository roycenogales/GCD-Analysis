import random
import timeit

intDiv = 0

##Best Case is O(1), as n could be the GCD of m, and it would take 2 iterations of euclid() to get the result. The worst case is O(lgm), as each time m%n is performed, the largest value possible is m/2-1
def euclid(m,n):
    global intDiv
    if n == 0:
        print("GCD is:", m)
        return m
    intDiv += 1
    ##recursively calls euclid to use find GCD of m and n.
    return euclid(n, m%n)

def getInput():
    m = int(input("Num 1:"))
    n = int(input("Num 2:"))
    return m, n

def start(m,n):
    euclid(m,n)

if __name__ == '__main__':
    ##m, n = getInput()
    print(timeit.timeit('m = random.randint(100,200); n = random.randint(50,99); start(m,n)', number=10, globals=globals()))
    print("Integer Divisions:", intDiv)
