#  Вычисляет возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)


# years

current_year = 2023
year_of_birth = 1988


w = str(current_year - year_of_birth)
print(w)

# 2. Найти недостающую часть кода (code_2):
#    - найдите остаток от x деленого на y
#    - полученый результ умножьте на 13
#    - извлеките квадратный корень из полученного результата (аналогично возведению в степень 0.5)
#    - возьмите целую часть от результата

# code 2 data
x = 152
y = 132

z = x % y

print(z)

z *= 13

print(z)

z **= 0.5

print(z)

print(int(z))

# 3. Соединить код в отдельную переменную
# пример:
# 475-12-967
# 4. Вывести строку используя доступные переменные:
# пример:
# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.

# code parts
code_1 = '354'
code_3 = 132

# name
user_name = 'John'
user_surname = 'Smith'

print('Hello',user_name + " " + user_surname + '.' + ' You are ' + w + ' years old.' + ' Your secret code is ' + code_1 + '-12-' + str(code_3))

