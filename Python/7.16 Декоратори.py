"""Декоратори- для модефікації функції за допомогою інших функцій, Тоюто функції які міняють інші функції
Використовується коли в декількох функціях є дублюючий код, і ми цей код виносим в декоратор"""

def decarator1(func):
    def inner():
        print('srart docorator')
        func()
        print('finish decorator')
    return inner


def say():
    print('Hello world')

d = decarator1(say) # Замиканієм Зараз зберегли функ inner в 'd' В-дь: <function decarator1.<locals>.inner at ....>, тобто в д наша функ inner
print(d)
d()

print(' -----------------------------------------------------------------------------------------')
# Щоб задекорувати функцію наприклад 'say', маємо назвати не якоюсь видуманою('d')нами зміною а самою назв функ, тобто 'say'
say = decarator1(say) # Замиканієм Зараз зберегли функ inner в 'd' В-дь: <function decarator1.<locals>.inner at ....>, тобто в д наша функ inner
print(say)
say()



print(' 2---------------------------- один-Декоратор з аргументами----------------------------------------------------')

def decarator2(func):
    # def inner (n,n2): #Шоб не писати кожен раз аргументи вручну краще писати *args,**kwargs
    def inner(*args, **kwargs):
        print('srart docorator')
        # func(n,n2) #Шоб не писати кожен раз аргументи вручну краще писати *args,**kwargs
        func(*args, **kwargs)
        print('finish decorator')
    return inner


def say2(name, surname):
    print('Hello', name, surname)


print(' -----------------------------------------------------------------------------------------')
# Щоб задекорувати функцію наприклад 'say', маємо назвати не якоюсь видуманою('d')нами зміною а самою назв функ, тобто 'say'
say2=decarator2(say2) # Замиканієм Зараз зберегли функ inner в 'd' В-дь: <function decarator1.<locals>.inner at ....>, тобто в д наша функ inner
print(say2)
say2('Vasia', 'Pizgabolow')


print(' 3---------------------------- два-Декоратора з аргументами----------------------------------------------------')

def dec_heder(func):
    # def inner (n,n2): #Шоб не писати кожен раз аргументи вручну краще писати *args,**kwargs
    def inner(*args, **kwargs):
        print('heder1')
        # func(n,n2) #Шоб не писати кожен раз аргументи вручну краще писати *args,**kwargs
        func(*args, **kwargs)
        print('heder2')
    return inner

def dec_table(func):
    def inner(*args, **kwargs):
        print('table-1')
        func(*args, **kwargs)
        print('table-2')
    return inner


def say3(name, surname, age):
    print('Hello', name, surname, age)

# На одну функцію задекорували  2 декоратора
say3=dec_table(dec_heder(say3)) # З
print(say3)
say3('Vasia', 'Pizgabolow', 30)

print("----------------------------------Покращення---------------------------------")
"""По правильному декоратори не дикорують так як зроблено вище, а НАВІШУЮТЬ @ """

@dec_heder # це робить те саме say4 = dec_heder(say4) - то як один декоратро з аргументом
def say4(name, surname, age):
    print('Hello', name, surname, age)


# say4=dec_table(dec_heder(say4)) # при навішуванні ця строчка не потрібна, навішування її заміняє
say4('Vasia', 'Pizgabolow', 30)

print("----------------------------------аналогічно можна навішати декілька декораторів---------------------------")

@dec_heder # це робить те саме say4 = dec_heder(say4) - то як один декоратро з аргументом
@dec_table
def say5(name, surname, age):
    print('Hello', name, surname, age)

say5('Vasia','Pizgabolow',30)