#easy_1
print("Привет, пользователь!")
name = input("Как тебя зовут? ")
print("Очень приятно,", name)

#easy_2
print("Введи любое целое число")
num = int(input())
print("Если к этому числу прибавить 2, получится", num + 2)

#easy_3
print(name, ", сколько тебе лет?")
age = int(input())
if age >= 18 :
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

#normal_1
i = int(input("Введите целое число: "))
while i < 0 or i > 10:
    print("Число должно находиться в границах 0..10. Повторите ввод")
    i = int(input())
else:
    print("При возведении в квадрат, получим: ", i**2)

#normal_2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
a = a + b
b = a - b
a = a - b
print(a, b)
