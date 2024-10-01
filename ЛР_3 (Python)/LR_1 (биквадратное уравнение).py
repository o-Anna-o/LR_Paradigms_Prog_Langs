import sys
import math
import time

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

def out_red(text):
    print("\033[31m{}".format(text))
def get_roots(a, b, c):
    result = []

    D = b * b - 4 * a * c
    print('Дискриминант = ', D, '\n')
    if D < 0:
        out_red('Корней нет')
    elif D > 0.0:
        tempVal1 = (-b + math.sqrt(D)) / (2 * a)
        tempVal2 = (-b - math.sqrt(D)) / (2 * a)

        if tempVal1 >= 0:
            root1 = math.sqrt(tempVal1)
            root2 = -math.sqrt(tempVal1)
            if root1 == -0:
                result.append(-root1)
            result.append(root1)
            result.append(root2)

        if tempVal2 >= 0:
            root3 = math.sqrt(tempVal2)
            root4 = -math.sqrt(tempVal2)
            result.append(root3)
            result.append(root4)

    elif D == 0.0:
        tempVal = -b / (2 * a)
        if tempVal >= 0:
            root1 = math.sqrt(tempVal)
            root2 = -math.sqrt(tempVal)
            result.append(root1)
            result.append(root2)


    result = set(result)
    return result

def main():
    # фиксируем время старта работы кода
    start = time.perf_counter()

    print("Данная программа предназначена для решения биквадратного уравнения\n")
    a = get_coefficient(1, 'Введите коэффициент A:')
    b = get_coefficient(2, 'Введите коэффициент B:')
    c = get_coefficient(3, 'Введите коэффициент C:')
    print('({:.0f})x^4 + ({:.0f})x^2 + ({:.0f}) = 0\n'.format(a, b, c))

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод корней
    for k, root in enumerate(roots, start=1):
        print('Корень {:.0f}: {:.2f}'.format(k, root))

    # фиксируем время окончания работы кода
    finish = time.perf_counter()

    # вычитаем время старта из времени окончания и выводим результат
    print('Время выполнения программы (мс) = {:.2f}'.format((finish - start)*1000))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
