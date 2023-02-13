from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        print('Из заданного числа не существует квадратног окорня')
    else: 
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет: {CalculateSquareRoot(your_number)}')


calc(-2)
