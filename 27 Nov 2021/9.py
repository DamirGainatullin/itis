mas1 = [[int(i) for i in input()], [int(i) for i in input()]]
mas2 = [[int(i) for i in input()], [int(i) for i in input()]]
dic1 = {}
dic2 = {}
print(mas1)
for i in range(len(mas1[0])):
    dic1[mas1[0][i]] = mas1[1][i]
for i in range(len(mas2[0])):
    dic2[mas2[0][i]] = mas2[1][i]

for i in range(len(mas1[0])):
    dic1[i] += dic2[i]

for i in range(len(mas1[0])):
    mas1[1][i] = dic1[i]

print(mas1)