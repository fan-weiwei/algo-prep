import math

def stars(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30 + '\n')
    return inner

@stars
def explain(string):
    print(string)

if __name__ == '__main__':
    explain('prints out all math functions')
    print(dir(math))

