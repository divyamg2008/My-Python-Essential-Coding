class new1:
    def __init__(self, s):
        self._s = s
    def __repr__(self):
        return(f"the repr is {self._s} 🙂")
    def __str__(self):
        return(f"the str is {self._s}")


s = new1("hola")
print(repr(s))
print(s)
print(ascii(s))
print(ord('🙂')) 
print(chr(128577))
print(chr(128574))