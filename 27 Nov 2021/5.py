n = 31234506772
ans = 0
i = 1
while n >= 1:
    ost = n % 10
    n //= 10
    if ost % 2 == 1:
        ost = ost * i + (ans % i)
        ans = (ans - ans % i)
        ans = ans * 10 + ost
        i *= 10
print(ans)
