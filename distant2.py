import time

# def printing(func):
#     def wrap():
#         print("Start")
#         start_time = time.time()
#         res = func()
#         print(time.time() - start_time)
#         print("End")
#         return res
#     return wrap
#
#
# @printing
# def example():
#     time.sleep(3)
#     print("some work")
#     return 123
#
# print(example())
f = open('result.txt', 'w', encoding='utf-8')


def lead_time(func):
    def wrap():
        start_time = time.time()
        f.write(f'Вызвана в: {time.ctime(start_time)} \n')
        res = func()
        end_time = time.time()
        f.write(f'Завершена в: {time.ctime(end_time)} \n')
        f.write(f'Выполнялось {end_time - start_time} секунд')
        f.close()
        return res

    return wrap


@lead_time
def example():
    time.sleep(1)
    return 'some work'


print(example())


def generator_of_primes_number(limit):
    for i in range(1, limit):
        simple = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                simple = False
        if simple:
            yield i


for val in generator_of_primes_number(100):
    print(val)
