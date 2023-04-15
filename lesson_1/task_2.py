# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

from utils import get_data_from_user
import math

def main():
    count_crane = int(get_data_from_user("Введите количество журавликов"))
    
    boy_count = math.floor(count_crane / 6)
    girl_count = count_crane - 2*boy_count
    
 
    print(f'Катя сделала {girl_count} журавликов, Петя и Вася по {boy_count} журавликов')

if __name__ == '__main__':
    main()