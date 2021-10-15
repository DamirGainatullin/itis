from random import randint


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


def print_list(first):
    current = first
    while current is not None:
        print(current.value, end=' ')
        current = current.next
    print('\n')


def counter(first): # Define list length
    if first is None:
        return None
    current = first
    i = 1
    while current.next is not None:
        i += 1
        current = current.next
    return i


def summ(first, second, third): #sum two lists
    if not first and not second:
        return None
    if not first:
        return second
    if not second:
        return first
    current = first
    current_2 = second
    current_3 = third
    while current is not None or current_2 is not None:
        if current is not None:
            a = current.value
            current = current.next
        else:
            a = 0
        if current_2 is not None:
            b = current_2.value
            current_2 = current_2.next
        else:
            b = 0
        summ = a + b
        if summ >= 10:
            summ -= 10
            current_3.next.value += 1
        current_3.value = summ
        if current_3.next is not None:
            current_3 = current_3.next
    return third

def bochka(a): # max S of water
    c = 0
    for i in range(len(a)):
        for j in range(len(a)):
            b = min(a[i], a[j])
            c = max(c, b * (j - i))
    return c

def revrse_list_by_links(first):
    if first is None:
        return first
    current = first
    a = None
    while current is not None:
        current.next, a, current = a, current, current.next
    return a

def get_value_by_index(first, index):
    if first is None:
        return first
    current = first
    i = 1
    while current is not None:
        if i == index:
            return current.value
        else:
            i += 1
            current = current.next

def switch(first, node1, node2):
    if first is None:
        return first
    current = first
    while current.next.value != node1:
        current = current.next
    current.next.value = node2
    current = current.next
    while current.next.value != node2:
        current = current.next
    current.next.value = node1
    return first


first = Node(1)
# second = Node(randint(1, 9))
# third = Node(0)
current = first
# current_2 = second
# current_3 = third
current.value = 1
# current_2.value = randint(1, 9)
# current_3.value = 0

for i in range(2, randint(9, 10)):
    # node = Node(randint(1, 9))
    node = Node(i)
    current.next = node
    current = current.next
# print_list(first)
# for i in range(randint(5, 10)):
#     node2 = Node(randint(1, 9))
#     current_2.next = node2
#     current_2 = current_2.next
# for i in range(max((counter(first), counter(second)))):
#     current_3.next = Node(0)
#     current_3 = current_3.next
# print_list(first)
# print_list(second)
# print_list(summ(first, second, third))
#
# a = [1, 5, 4, 2, 4, 1]
# print(bochka(a))
# print_list(revrse_list_by_links(first))
# print(get_value_by_index(first, 5))
# print_list(switch(first, 2, 5))