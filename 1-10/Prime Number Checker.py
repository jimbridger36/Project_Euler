
class primes:
    # location of int i is i // 2
    # location of 2 is 0
    primes = [2,3]
    sieve = []

    def __init__(self):
        pass

    def setupsieve(self, size):
        start = len(self.sieve)
        if size % 2 == 1:
            print('doing primes up to ' + str(size+1))
        if size < start:
            print('size is smaller than current there is no point sieving')
            return 0
        self.sieve = self.sieve + [False for i in range(start, size)]

        for i in range(start//2, size//2):
            if





    def primescheck(self,num):
        #cdef ind i
        for i in range(0,len(self.primes)):
            if num % self.primes[i] == 0:
                return False
        return True





