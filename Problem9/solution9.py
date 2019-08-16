# a + b + c = 1000
# a^2 + b^2 = c^2

# c = 1000 - a - b
# c^2 = (1000 - a - b)^2
# c^2 = (1000 - a - b)(1000 - a - b)
# c^2 = 1000000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab + b^2
# c^2 = 1000000 - 2000a - 2000b + 2ab + a^2 + b^2
# a^2 + b^2 = 1000000 - 2000a - 2000b + 2ab + a^2 + b^2
# 1000000 = 2000a + 2000b - 2ab
# 500000 = 1000a + 1000b - ab
# a = 200 , b = 375 , c = 425

a = b = c = 1
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if ((a*a + b*b) == c*c):
            print(f"a is {a}, b is {b}, c is {c}")
            producto=a*b*c
            print(f"a*b*c is {producto}")
