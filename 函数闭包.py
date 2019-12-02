glob = 3
def func(x):
    y = x + glob
    def inner():
        return y + 1
    return inner, abs
a, b = func(2)
print(a())
print(b)