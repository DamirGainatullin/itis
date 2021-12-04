def get_int(n):
    ans = []
    while n >= 1:
        ans.append(n % 10)
        n //= 10
    return ans

a = []
otv = [0 for i in range(10)]
n = int(input())
for i in range(n):
    a.append([int(i) for i in input().split()])
for x in a:
    for y in x:
        for z in get_int(y):
            otv[z] += 1
for i in range(len(otv)):
    print(f'{i}: {otv[i]} times')