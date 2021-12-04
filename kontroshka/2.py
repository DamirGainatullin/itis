def fact(n):
    ans = 1
    while n != 1:
        ans *= n
        n -= 1
    return ans

n = int(input())
x = int(input())
stepen = x
summ = 0
for k in range(1, n + 1):
    stepen = stepen * x * x
    if k % 2 == 1:
        summ += (-1 * stepen)/(fact(k) + x)
    else:
        summ += (stepen)/(fact(k) + x)
print(summ)
