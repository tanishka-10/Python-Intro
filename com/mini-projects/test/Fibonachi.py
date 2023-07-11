print(1)
x = 2
y = 1
for counter in range(1,1000000):
    t = x + y
    print(t)
    y = x
    x = t