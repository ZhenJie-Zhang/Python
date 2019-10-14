s = "Hello world, welcome to Python world"
print(s.startswith("Hello"))
print(s.startswith("hello"))
print(s.startswith("H"))
print(s.startswith("h"))

s1 = 'hello.py'
print(s1.endswith(".py"))

print(s.find("world"))
print(s.find("World"))
print(s.rfind("world"))
print(len(s))

s2 = "Hello world, welcome to Python world Hello world, welcome to Python world"
print(s2.count('world'))

print('count method')
count = 0
index = s2.find("world")
while index != -1:
    count += 1
    index = s2.find("world", index + 1)
print(count)

print(s2.count('world'))

s = "Hello world, welcome to Python world"
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())

print(s2.replace('Python', 'Java'))

s = '    Python     '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

s = 'Python'
print(s.ljust(10))
print(s.rjust(10))
print(s.center(10))