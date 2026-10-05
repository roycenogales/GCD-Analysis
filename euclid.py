import timeit

##Best Case is O(1), as n could be the GCF of m, and it would take 2 iterations of euclid() to get the result. The worst case is O(lgm), as each time m%n is performed, the largest value possible is m/2-1
def euclid(m,n):
    if n == 0:
        ##print("GCF is:", m)
        return m
    ##recursively calls euclid to use find GCF of m and n.
    return euclid(n, m%n)

def getInput():
    m = int(input("Num 1:"))
    n = int(input("Num 2:"))
    return m, n

def start(m,n):
    euclid(m,n)

if __name__ == '__main__':
    m, n = getInput()
    print(timeit.timeit('start(m,n)', number=100, globals=globals()))
