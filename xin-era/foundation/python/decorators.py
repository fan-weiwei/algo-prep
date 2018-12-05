def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

# *******************


class Object:

    @property
    def var(self):
        return self._var + 1

    @var.setter
    def var(self, value):
        self._var = value



if __name__ == '__main__':
    printer("Hello")
    print('\n' * 2)

    obj = Object()
    obj.var = 2
    print(obj.var)