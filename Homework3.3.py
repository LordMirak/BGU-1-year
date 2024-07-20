slowar={}
try:
    with open('input.txt', 'r') as inp:
        for i in inp:
            a = i.split(' : ')
            name = a[0]
            subjects = a[1].rstrip(',\n').split(', ')
            for subject in subjects:
                if subject not in slowar:
                    slowar[subject] = [name]
                else:
                    slowar[subject].append(name)
        b = input('Введите название предмета: ')
        if b in slowar:
            print(*slowar[b], sep='\n')
except FileNotFoundError:
    print('This file does not exist. Please come back later')