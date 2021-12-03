import math
s = 1234
list_s = [int(i) for i in str(s)[::-1]]
print(sum(list_s[0: len(list_s): 2]) - sum(list_s[1: len(list_s): 2]))



s = list(reversed([int(i) for i in str(s)]))
ans = 0
for i in range(len(s)):
    a = s[i] * int(math.pow(-1, i))
    ans += a
print(ans)


ans = 0
# s = list(reversed([int(i) for i in str(s)]))
for i in range(len(s)):
    if i % 2 == 0:
        ans += s[i]
    else:
        ans -= s[i]
print(ans)