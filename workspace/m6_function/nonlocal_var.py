def func():
    x = 10

    def get_x():
        return x

    def set_x(n):
        nonlocal x
        x = n
    return get_x, set_x


getX, setX = func()
print(getX())
setX(20)
print(getX())