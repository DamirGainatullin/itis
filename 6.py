a = [2, 4, 5, 6, 7 ,1 ,22, 11]
b = 13
a = sorted(list(filter(lambda x: x < b, a)))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] + a[j] == b:
            print(a[i], a[j])
            exit(0)


