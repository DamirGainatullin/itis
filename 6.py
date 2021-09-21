a = [12, 4, 5, 6, 7 ,1 ,22, 11]
b = 24
a = sorted(list(filter(lambda x: x < b, a)))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] + a[j] == b and i != j:
            print(a[i], a[j])
            exit(0)


