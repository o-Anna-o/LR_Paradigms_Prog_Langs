import sys
import math
import time

class BiQuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_roots(self):
        result = []
        D = self.b ** 2 - 4 * self.a * self.c
        print('Дискриминант = ', D, '\n')

        if D > 0.0:
            tempVal1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            tempVal2 = (-self.b - math.sqrt(D)) / (2 * self.a)

            if tempVal1 >= 0:
                result.append(math.sqrt(tempVal1))
                result.append(-math.sqrt(tempVal1))

            if tempVal2 >= 0:
                result.append(math.sqrt(tempVal2))
                result.append(-math.sqrt(tempVal2))

        elif D == 0.0:
            tempVal = -self.b / (2 * self.a)
            if tempVal >= 0:
                result.append(math.sqrt(tempVal))
                result.append(-math.sqrt(tempVal))

        return result

    @staticmethod
    def get_coefficient(index, prompt):
        while True:
            try:
                coef_str = sys.argv[index]
                coef = float(coef_str)
                return coef
            except (IndexError, ValueError):
                print(prompt)
                coef_str = input()
                try:
                    coef = float(coef_str)
                    return coef
                except ValueError:
                    print("Некорректное значение. Попробуйте снова.")

def main():
    # фиксируем время старта работы кода
    start = time.time()

    print("Данная программа предназначена для решения биквадратного уравнения\n")
    a = BiQuadraticEquation.get_coefficient(1, 'Введите коэффициент A:')
    b = BiQuadraticEquation.get_coefficient(2, 'Введите коэффициент B:')
    c = BiQuadraticEquation.get_coefficient(3, 'Введите коэффициент C:')

    equation = BiQuadraticEquation(a, b, c)
    print('({:.0f})x^4 + ({:.0f})x^2 + ({:.0f}) = 0\n'.format(equation.a, equation.b, equation.c))

    # Вычисление корней
    roots = equation.get_roots()

    # Вывод корней
    for k, root in enumerate(roots, start=1):
        print('Корень {:.0f}: {:.2f}'.format(k, root))

    # фиксируем время окончания работы кода
    finish = time.time()
    
    res_msec = (finish - start) * 1000
    print('Время работы (мс): ', res_msec)

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
