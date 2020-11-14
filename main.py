from Ksiazka import Ksiazka, customException

if __name__ == '__main__':
    ksiazka = Ksiazka('Python. Instrukcje dla programisty',
                      'Eric Matthes',
                      'Helion',
                      2000)
    print(ksiazka);

    try:
        ksiazka.zmienRokWydania(-1)
    except customException:
        print('Podales rok mniejszy < 0')

    try:
        ksiazka.zmienWydawnictwo("")
    except customException:
        print('Wydawnictwo nie moze byc puste')


