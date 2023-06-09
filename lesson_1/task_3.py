#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

from utils import get_data_from_user

def main():
    data = get_data_from_user("Введите номер билета")
    left_side = data[0] + data[1] + data[2]
    rigth_side = data[3] + data[4] + data[5]
    is_lucky = left_side == rigth_side
    result = "счастливый" if is_lucky else "несчастливый"

    print(f"билет № {data} - {result}")

if __name__ == '__main__':
    main()