v = 0
a = 'input.txt'
x = []
try:
    with open(a, 'r') as grade:
        for i in grade:
            z = i.split(',')
            x.append(z)
            print(i.strip())
            v = v + int(z[1])
    sr = v / (len(x))
    print('Среднее оценок: ')
    print(sr)
    with open('output.txt', 'w') as superior:
        for i in x:
            if int(i[1]) > sr:
                print(i[0], file=superior)

except FileNotFoundError:
    print('This file does not exist. Please come back later')



