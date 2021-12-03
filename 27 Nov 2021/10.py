def big_Check(a: list):
    def check(a: int):
        if (a % 10) % 2 == 0:
            while a > 10:
                a //= 10
                if a % 2 == 1:
                    return False
        else:
            while a > 10:
                a //= 10
                if a % 2 == 0:
                    return False
        return True
    ans = 0
    for i in a:
        if (1 <= i // 100 <= 10 or 1 <= i // 10000 <= 10) and check(i):
            ans += 1
    if ans == 2:
        return True
    else:
        return False

n = int(input())
a = [int(input()) for i in range(n)]
print(BicCheck(a))

