# Найдите сумму цифр трехзначного числа
def get_data_from_user():
    return input()

def main():
    print("Введите трехзначное число")
    data = get_data_from_user()

    print(f'{data[0]} + {data[1]} + {data[2]} = {int(data[0]) + int(data[1]) + int(data[2])}')

main()