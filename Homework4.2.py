def euclidean_algorithm(x, y):
    if x == 0 and y == 0:
        return False
    if x == 0 or y == 0:
        return x + y
    else:
        if x < y:
            return euclidean_algorithm(x, y % x)
        else:
            return euclidean_algorithm(x % y, y)


try:
    a = int(input('Введите 1 число: '))
    b = int(input('Введите 2 число: '))
    print(euclidean_algorithm(a, b))
except ValueError:
    print('Вводите строго числа!')






