import random

# Zadanie 01
# Napisze metode ktora wykona sie x razy - podaje uzytkownik x
# Metoda generuje x razy dowolna wartosc i weryfikuje czy jest podzielna przez 2
# zwraca dwie wartosci: liczby podzielne przez jako liste oraz dowolny komunikat

def getRandomNumbers(x):
    lista = []
    for i in range(0, x):
        temp = random.randint(1,50)
        if temp % 2 == 0:
            print(f'liczba {temp} jest podzielna przez 2')
            lista.append(temp)
    return 'Lista losowych liczb podzielnych przez 2', lista



if __name__ == '__main__':
    msg, lista = getRandomNumbers(50)
    print(f'{msg} {lista}')


