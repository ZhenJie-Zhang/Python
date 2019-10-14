# x = 10
# y = 11
#
#
# def main():
#     x = 20
#     z = 100
#     print(x)
#     print(y)
#     print(z)
#
#
# main()
# print(x)
# print(y)

# x = 10
# def outer():
#     x = 20
#     def inner():
#         x = 30
#         print(x)
#     print(x)
#     inner()
# outer()
# print(x)

# x = 10
# y = 11
#
# def main():
#     x =20
#     print(x)
#     global y
#     y = 22
#     print(y)
#
# main()
# print(x)
# print(y)

# x = 10
# def outer():
#     x = 20
#
#     def inner():
#         nonlocal x
#         print(x)
#         x = 30
#
#     inner()
#     print(x)
#
# outer()
# print(x)

x = 10
def outer():
    x = 20

    def inner():
        global x
        print(x)
        x = 30

    inner()
    print(x)

outer()
print(x)

