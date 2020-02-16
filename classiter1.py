import random
class randnum:
    def __init__(self, n =1, r = 5):
        self._n = n
        self._r = r
        self._count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self._count < self._n:
            self._count += 1
            return random.randint(0, self._r)
            
            
        else:
            raise StopIteration

def main():
    for i in randnum(5,4):
        print (i)

if __name__ == "__main__":
    main()