class food:
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'item' in kwargs:
            self._item = kwargs['item']
        if 'number' in kwargs:
            self._number = kwargs['number']

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def item(self, i=None):
        if i:
            self._item = i
        try:
            return self._item
        except AttributeError:
            return None

    def number(self, n=None):
        if n:
            self._number = n
        try:
            return self._number
        except AttributeError:
            return None

    def __str__(self):
        return f'The {self.type()} eats {self.item()} {self.number()} times'


class Duck(food):
    def __init__(self, **kwargs):
        self._type = 'Duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)


class Dog(food):
    def __init__(self, **kwargs):
        self._type = 'Dog'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, a):
        return f"{a} kills {self.type()}"

a0 = Duck(type = 'ho', number = 6, item = 'weeds')
a0.number(10)
a0.type('hola')
print(a0)
a1 = Dog(type ='Roger', number = 2, item = 'chicken')
print(a1)
print(a1.kill('tiger'))
