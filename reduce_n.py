import random
import timeit

##Best case is O(1), since min(m,n) is also the GCD, while the Worst case is O(min(m,n)-1).
def consecInt(m,n):
    t = min(m,n)
    ##at most, this while loop runs min(m,n)-1 times
    while t > 0:
        if m % t == 0 and n % t == 0:
            print("GCD is:", t)
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
    ##m, n = getInput()
    print(timeit.timeit('m = random.randint(100,200); n = random.randint(50,99); start(m,n)', number=10, globals=globals()))
