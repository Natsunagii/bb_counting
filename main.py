import re
info = "Перед тем, как добавлять все значения с заказов блейзинга на проверку выплаты нужно:\n* Скоропировать массив данных с выплатой\n* Вставить в строку браузера\n* И уже полученый результат отправить в input"
print(info)
input_string = input("Введите значения в формате 'S23999DFD8 (8.55), ...': ")
values = re.findall(r'\((.*?)\)', input_string)
sum_values = 0

for value in values:
    try:
        sum_values += float(value)
    except ValueError:
        print(f"Пропущено значение: {value}, так как оно не может быть преобразовано в число.")

print(sum_values)