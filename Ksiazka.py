class Ksiazka:
    def __init__(self, tytul = '', autor = '', wydawnictwo = '', rokWydania = None):
        self.tytul = tytul
        self.autor = autor
        self.wydawnictwo = wydawnictwo
        self.rokWydania = rokWydania

    def zmienWydawnictwo(self, wydawnictwo):
        if wydawnictwo == '':
            raise customException
        else:
            self.wydawnictwo = wydawnictwo;

    def zmienRokWydania(self, rokWydania):
        if rokWydania < 0:
            raise customException
        else:
            self.rokWydania = rokWydania;

    def __str__(self):
        return 'Tytul: {s.tytul} | Autor: {s.autor} | wydawnictwo: {s.wydawnictwo} | rokWydania : {s.rokWydania}'.format(s=self)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class customException(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    pass