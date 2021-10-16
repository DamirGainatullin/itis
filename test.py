a = [1, 3, 3 ,4, 5, 6, 7]
b = [4, 4, 6, 7, 8, 9, 10, 11]
res = []
i = 0
j = 0
while len(res) < len(a) + len(b):
    if a[i] <  b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
    if i > len(a) - 1:
        while j < len(b):
            res.append(b[j])
            j += 1
    if j > len(a) - 1:
        while i < len(a):
            res.append(a[i])
            i += 1
print(res)


a = [11, 43, 43, 14, 16, 17, 17]
print(a)
max1 = a[0]
i = 1
while a[0] == a[i]:
    i += 1
max2 = a[i]
if max2 > max1:
    max2, max1 = max1, max2
j = i + 1
while a[i] == a[j]:
    j += 1
max3 = a[j]
if max3 > max2:
    if max3 > max1:
        max1, max3 = max3, max1
    else:
        max2, max3 = max3, max2
test = [max1, max2, max3] #Выбираем первые три уникальные значения и сортируем их
# print(test)
for i in range(len(a)):
    if a[i] in [max1, max2, max3]:
        continue
    if a[i] > max3:
        if a[i] > max2:
            if a[i] > max1:
                max2 = max1
                max1 = a[i]
            else:
                max3 = max2
                max2 = a[i]
        else:
            max3 = a[i]
    # print([max1, max2, max3])
print(max3)
