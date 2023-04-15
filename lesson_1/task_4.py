#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

from utils import get_data_from_user

def main():
    n = int(get_data_from_user("Введите ширину шоколадки (n)"))
    m = int(get_data_from_user("Введите длину шоколадки (m)"))
    k = int(get_data_from_user("Введите количество долек (k)"))

    is_square = k % m == 0 or k % n == 0
    result = "да, можем" if is_square else "нет, не можем"

    print(f"{result} разломить на два прямоугольника")

if __name__ == '__main__':
    main()