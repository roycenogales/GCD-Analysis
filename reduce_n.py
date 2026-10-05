import timeit

##Best case is O(1), since min(m,n) is also the GCF, while the Worst case is O(min(m,n)-1).
def consecInt(m,n):
    t = min(m,n)
    ##at most, this while loop runs min(m,n)-1 times
    while t > 0:
        if m % t == 0 and n % t == 0:
            ##print("GCF is:", t)
            return t
        else:
            t -= 1

def getInput():
    m = int(input("Num 1:"))
    n = int(input("Num 2:"))
    return m, n

def start(m,n):
    consecInt(m,n)

if __name__ == '__main__':
    m, n = getInput()
    print(timeit.timeit('start(m,n)', number=100, globals=globals()))
