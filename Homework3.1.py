spisek=[]
s=int(input('Введите минимальное число жителей: '))
try:
    with open('cities.txt', 'r') as city:
        for i in city:
            a = i.split(':')
            spisek.append(a)
        with open('filtered_cities.txt', 'w') as filter:
            spisek.sort(key=lambda x: x[0])
            for i in spisek:
                if int(i[1]) > s:
                    d = ':'.join(i).strip()
                    print(d, file=filter)
except FileNotFoundError:
    print('This file does not exist. Please come back later')
