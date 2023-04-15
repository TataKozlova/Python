#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from utils import get_data_from_user
from math import sqrt

def calculate(b, c):
    D = b*b - 4*c  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]

def main():
    s = int(get_data_from_user("Введите сумму (S)"))
    p = int(get_data_from_user("Введите произведение (P)"))

    result = calculate(s, p)

    print(f"первое число - {int(result[0])}, второе число - {int(result[1])}")

if __name__ == '__main__':
    main()