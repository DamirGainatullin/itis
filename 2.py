records = [
    ['chi', 500],
    ['beta', 5000],
    ['alpha', 5000],
    ['oleg', 5000]
]
grades={}
for iten in records:
    if iten[1] in grades.keys():
        grades[iten[1]].append(iten[0])
    else:
        grades[iten[1]]=[iten[0]]
print(grades)



a={}
a={1:250, 2:83939, 4:"klk", 3:"дамир пидор"}
print(a[3])