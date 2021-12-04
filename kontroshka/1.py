def check(a):
    while a > 10:
        a //= 10
        if a % 2 == 1:
            return False
    return True

n = int(input())
a = [int(input()) for i in range(n)]
for i in a:
    if check(i):
        print('True')
        exit(0)
print('False')