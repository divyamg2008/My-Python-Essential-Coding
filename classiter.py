class inclusive_range:
    def __init__(self, *args):
        self._start = 0
        self._step = 1
        if len(args) < 1:
            raise TypeError(f"Expected 1, recieved {len(args)}")
        elif len(args) == 1:
            self._stop = args[0]
        elif len(args) == 2:
            self._start, self._stop = args
        elif len(args) == 3:
            self._start, self._stop, self._step = args
        else:
            raise TypeError(f"Expected max 3, recieved {len(args)}")
        self._next = self._start
    
    def __iter__(self):
        return(self)
    

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

for n in inclusive_range(2,9, 3):
    print(n, end=' ')