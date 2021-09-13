a = '-eto polindrom?, -Da-'
ans = ''
true_symbl = [chr(i) for i in range(48, 58)]
true_symbl.extend([chr(i) for i in range(65, 91)])
true_symbl.extend([chr(i) for i in range(97, 123)])

b = []
s = []
for i in a:
    if i not in true_symbl:
        b.append(s)
        b.append([i])
        s = []
    else:
        s.append(i)
b.append(s)
for i in b:
    for j in range(len(i) // 2):
        i[j], i[len(i) - j - 1] = i[len(i) - j - 1], i[j]
ans = [j for i in b for j in i]
print(''.join(ans))
