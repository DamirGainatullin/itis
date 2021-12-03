n = 12345
ans = n * 10 + 1
i = 1
while n >= 1:
    n //= 10
    i *= 10
ans = i * 10 + ans
print(ans)

