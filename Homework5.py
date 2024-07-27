import random as r

food_base = 0
dict_animals = {
    'Boba': [],
    'Biba': [],
    'Slon': [],
    'Reaper': [],
    'Giraffe': [],
    'Vvardvark': [],
    'Mouse': [],
    'Wolf': [],
    'Kranich': [],
    'Adler': [],
    'Schwan': [],
    'Viverna': []
}


class Animal:
    def __init__(self, animal_id, max_age, kind_name, size, sex, hunger, habitat, age=0):
        self.animal_id = animal_id
        self.kind_name = kind_name
        self.max_age = max_age
        self.age = age
        self.size = size
        self.hunger = hunger
        self.sex = sex
        self.is_alive = True
        self.habitat = habitat

    def death(self):
        global food_base
        food_base += self.size
        self.is_alive = False

    def growing(self):
        self.age += 1
        if self.age > self.max_age:
            self.death()

    def starvation(self):
        self.hunger -= 9
        if self.hunger < 10:
            self.death()


class Predator(Animal):
    def __init__(self, animal_id, max_age, kind_name, size, sex, hunger, habitat, type_of_food, age=0):
        super().__init__(animal_id, max_age, kind_name, size, sex, hunger, habitat, age)
        self.type_of_food = type_of_food
        self.is_herbivorous = False

    def hunting(self):
        h = r.choice([True, False])
        if h:
            self.hunger += 53
            if self.hunger > 100:
                self.hunger = 100
            return True
        else:
            self.hunger -= 16
            if self.hunger < 10:
                self.death()
            return False


class Herbivorous(Animal):
    def __init__(self, animal_id, max_age, kind_name, size, sex, hunger, habitat, age=0):
        super().__init__(animal_id, max_age, kind_name, size, sex, hunger, habitat, age)
        self.is_herbivorous = True

    def feeding(self):
        global food_base
        if food_base > 0:
            food_base -= 1
            self.hunger += 26
            if self.hunger > 100:
                self.hunger = 100
        else:
            self.starvation()


class Boba(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 15, 'Boba', 13, sex, hunger, 'Вода')


class Biba(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 17, 'Biba', 20, sex, hunger, 'Вода', ['Boba', ])


class Slon(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 20, 'Slon', 5, sex, hunger, 'Вода')


class Reaper(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 100, 'Reaper', 50, sex, hunger, 'Вода', ['Slon', 'Biba', 'Boba'])


class Giraffe(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 20, 'Giraffe', 30, sex, hunger, 'Суша')


class Vvardvark(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 10, 'Vvardvark', 15, sex, hunger, 'Суша', ['Giraffe'])


class Mouse(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 8, 'Mouse', 3, sex, hunger, 'Суша')


class Wolf(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 10, 'Wolf', 10, sex, hunger, 'Суша', ['Vvardvark', 'Giraffe'])


class Kranich(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 10, 'Kranich', 15, sex, hunger, 'Воздух')


class Adler(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 25, 'Adler', 15, sex, hunger, 'Воздух', ['Kranich', 'Wolf', 'Mouse', ])


class Schwan(Herbivorous):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 30, 'Schwan', 20, sex, hunger, 'Воздух')


class Viverna(Predator):
    def __init__(self, animal_id, sex, hunger):
        super().__init__(animal_id, 50, 'Viverna', 40, sex, hunger, 'Воздух',
                         ['Schwan', 'Adler', 'Kranich', 'Vvardvark'])


def water_reproduction(m_animal, f_animal):
    if m_animal.hunger > 50 and f_animal.hunger > 50:
        names = input('Введите именя 10 новорожденных через пробел: ').split(' ')
        c = m_animal.kind_name
        for i in names:
            s = r.choice(['Male', 'Female'])
            if c == 'Boba':
                dict_animals[c].append(Boba(i, s, 23))
            elif c == 'Biba':
                dict_animals[c].append(Biba(i, s, 23))
            elif c == 'Slon':
                dict_animals[c].append(Slon(i, s, 23))
            elif c == 'Reaper':
                dict_animals[c].append(Reaper(i, s, 23))
    else:
        print('В настоящий момент икубатор не работает, вернитесь позже.')


def ground_reproduction(m_animal, f_animal):
    if m_animal.hunger > 20 and f_animal.hunger > 20 and m_animal.age > 5 and f_animal.age > 5:
        names = input('Введите именя 2 новорожденных через пробел: ').split(' ')
        c = m_animal.kind_name
        for i in names:
            s = r.choice(['Male', 'Female'])
            if c == 'Giraffe':
                dict_animals[c].append(Giraffe(i, s, 64))
            elif c == 'Vvardvark':
                dict_animals[c].append(Vvardvark(i, s, 64))
            elif c == 'Mouse':
                dict_animals[c].append(Mouse(i, s, 64))
            elif c == 'Wolf':
                dict_animals[c].append(Wolf(i, s, 64))
    else:
        print('В настоящий момент икубатор не работает, вернитесь позже.')


def sky_reproduction(m_animal, f_animal):
    if m_animal.hunger > 42 and f_animal.hunger > 42 and m_animal.age > 3 and f_animal.age > 3:
        names = input('Введите именя 4 новорожденных через пробел: ').split(' ')
        c = m_animal.kind_name
        for i in names:
            s = r.choice(['Male', 'Female'])
            if c == 'Kranich':
                dict_animals[c].append(Kranich(i, s, 64))
            elif c == 'Adler':
                dict_animals[c].append(Adler(i, s, 64))
            elif c == 'Schwan':
                dict_animals[c].append(Schwan(i, s, 64))
            elif c == 'Viverna':
                dict_animals[c].append(Viverna(i, s, 64))
        else:
            print('В настоящий момент икубатор не работает, вернитесь позже.')


a = ''
while a != 0:
    a = int(input('''Что вы хотите сделать:
    1 - Модуляция движения времени
    3 - Увеличить кормовую базу
    4 - Добавить одно новое животное
    5 - Просмотреть характеристики каждой особи
    6 - Вывести информацию о всех видах животных
    7 - Запустить процесс размножения
    0 - End \n'''))

    if a == 1:
        for i in dict_animals.values():
            for animal in i:
                if animal.is_alive:
                    animal.growing()
                    if animal.is_herbivorous:
                        animal.feeding()
                    else:
                        target_kind = r.choice(animal.type_of_food)
                        if len(dict_animals[target_kind]) > 0:
                            g = r.choice(dict_animals[target_kind])
                            if animal.hunting():
                                g.is_alive = False
                        else:
                            animal.hunger -= 16
                            if animal.hunger < 10:
                                animal.death()
                    if animal.hunger < 10:
                        animal.death()



    elif a == 3:
        print(f'Текущий кормовой запас: {food_base}')
        b = int(input('Введите число, на которое необходимо увеличить кормовой запас: '))
        food_base += b
        print(f'Текущий кормовой запас: {food_base}')

    elif a == 4:
        c = input(f'''Введите вид живодного, которое хотите создать: 
        {', '.join(dict_animals.keys())} \n''')
        s = input('Выберите пол животного. Для этого введите Male или Female:')
        i = input('Введите уникальное имя особи: ')
        if c == 'Boba':
            dict_animals[c].append(Boba(i, s, 23))
        elif c == 'Biba':
            dict_animals[c].append(Biba(i, s, 23))
        elif c == 'Slon':
            dict_animals[c].append(Slon(i, s, 23))
        elif c == 'Reaper':
            dict_animals[c].append(Reaper(i, s, 23))
        elif c == 'Giraffe':
            dict_animals[c].append(Giraffe(i, s, 73))
        elif c == 'Vvardvark':
            dict_animals[c].append(Vvardvark(i, s, 73))
        elif c == 'Mouse':
            dict_animals[c].append(Mouse(i, s, 73))
        elif c == 'Wolf':
            dict_animals[c].append(Wolf(i, s, 73))
        elif c == 'Kranich':
            dict_animals[c].append(Kranich(i, s, 64))
        elif c == 'Adler':
            dict_animals[c].append(Adler(i, s, 64))
        elif c == 'Schwan':
            dict_animals[c].append(Schwan(i, s, 64))
        elif c == 'Viverna':
            dict_animals[c].append(Viverna(i, s, 64))

    elif a == 5:
        for n in dict_animals:
            for i in dict_animals[n]:
                print(f'''
                Вид: {n}
                Имя: {i.animal_id}
                Пол: {i.sex}
                Сытость: {i.hunger}
                Возраст: {i.age}''')

    elif a == 6:
        print('''
         1. Вид Boba
         Травоядный
         Максимальный возраст 15
         Размер 13
         Среда обитания: Вода
         
         2. Вид Biba
         Хищник
         Максимальный возраст 17
         Размер 20
         Среда обитания: Вода
         Охотится на Boba
         
         3. Вид Slon
         Травоядный
         Максимальный возраст 120
         Размер 5
         Среда обитания: Вода
         
         4. Вид Reaper
         Хищник
         Максимальный возраст 100
         Размер 50
         Среда обитания: Вода
         Охотится на Slon, Biba, Boba
         
         5. Вид Giraffe
         Травоядный
         Максимальный возраст 20
         Размер 30
         Среда обитания: Суша
         
         6. Вид Vvardvark
         Хищник
         Максимальный возраст 10
         Размер 15
         Среда обитания: Суша
         Охотится на Giraffe
         
         7. Вид Mouse
         Травоядный
         Максимальный возраст 5
         Размер 3
         Среда обитания: Суша
         
         8. Вид Wolf
         Хищник
         Максимальный возраст 7
         Размер 10
         Среда обитания: Суша
         Охотится на Vvardvark, Giraffe
         
         9. Вид Kranich
         Травоядный
         Максимальный возраст 10
         Размер 15
         Среда обитания: Воздух
         
         10. Вид Adler
         Хищник
         Максимальный возраст 25
         Размер 15
         Среда обитания: Воздух
         Охотится на Kranich, Wolf, Mouse
         
         11. Вид Schwan
         Травоядный
         Максимальный возраст 30
         Размер 20
         Среда обитания: Воздух
         
         12. Вид Viverna
         Хищник
         Максимальный возраст 50
         Размер 40
         Среда обитания: Воздух
         Охотится на Schwan, Adler, Kranich, Vvardvark''')

    elif a == 7:
        kind_name = input('Введите тот вид, который хотите размножить: ')
        list_animals_female = []
        list_animals_male = []
        for animal in dict_animals[kind_name]:
            if animal.sex == 'Male':
                list_animals_male.append(animal)
            else:
                list_animals_female.append(animal)
        print(f'Список женских особей вида:{kind_name}:{[x.animal_id for x in list_animals_female]}')
        print(f'Список мужских особей вида:{kind_name}:{[x.animal_id for x in list_animals_male]}')
        m_animal = input('Введите имя мужской особи: ')
        for i in list_animals_male:
            if i.animal_id == m_animal:
                m_animal = i
        f_animal = input('Введите имя женской особи: ')
        for i in list_animals_female:
            if i.animal_id == f_animal:
                f_animal = i
        if m_animal.habitat == 'Суша':
            ground_reproduction(m_animal, f_animal)
        elif m_animal.habitat == 'Вода':
            water_reproduction(m_animal, f_animal)
        else:
            sky_reproduction(m_animal, f_animal)


    for i in dict_animals:
        list_with_alive_animals = []
        for animal_index in range(len(dict_animals[i])):
            if dict_animals[i][animal_index].is_alive:
                list_with_alive_animals.append(dict_animals[i][animal_index])
        dict_animals[i] = list_with_alive_animals

print('Конец игры!')
