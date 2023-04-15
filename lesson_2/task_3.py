#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

from utils import get_data_from_user

def main():
    n = int(get_data_from_user("Введите число N"))
    p = 1
    while n > 2**p:
        p = p + 1

    for i in range(1,p):
        print(f"2 в степени {i} = {2**i}, это меньше {n}")


if __name__ == '__main__':
    main()