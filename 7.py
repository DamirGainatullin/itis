a = 'abcdexy dfs'

# print(a[::-1])

a = list(a)
for i in range(len(a) // 2):
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

print(''.join(a))