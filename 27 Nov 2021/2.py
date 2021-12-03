s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
ans = []

for i in range(0, len(s) - 10):
    index = i + 10
    if s[i: index] in s[index:]:
        ans.append(s[i: index])

print(ans)