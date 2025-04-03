try:
    numero1 = int(input('Numero1: '))
    numero2 = int(input('Numero2: '))
    division = numero1/numero2
    print(division)
except ValueError:
    print('Error en conversion')
except ZeroDivisionError:
    print('divison por cero')