a = [1, 2, 3, 4]
i = len(a) - 1
if a[i] == 9:
    while a[i] == 9:
        a[i] = 0
        i -= 1
    if i == -1:
        a.append(1)
        a[0], a[-1] = a[-1], a[0]
else:
    a[i] += 1
print(a)
