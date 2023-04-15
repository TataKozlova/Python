from utils import get_data_from_user
# Найдите сумму цифр трехзначного числа

def main():
    data = get_data_from_user("Введите трехзначное число")

    print(f'{data[0]} + {data[1]} + {data[2]} = {int(data[0]) + int(data[1]) + int(data[2])}')

if __name__ == '__main__':
    main()