n = 1892345
maxx = 0
while n >= 1:
    ost = n % 10
    n //= 10
    if  ost > maxx:
        maxx = ost
print(maxx)