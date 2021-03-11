# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"

d1,d2,d3,d4 = ip.split('.')
#print("{:<10}{:<10}{:<10}{:<10}".format(ip.split('.')))
b1,b2,b3,b4 = str(bin(int(d1)))[2:],str(bin(int(d2)))[2:],str(bin(int(d3)))[2:],str(bin(int(d4)))[2:]

#print("{:b}".format(result))

print("{:<10}{:<10}{:<10}{:<10}".format(d1,d2,d3,d4))
print("{:>08b}  {:>08b}  {:>08b}  {:>08b}".format(int(d1),int(d2),int(d3),int(d4)))
#print("{}{}{}{}".format(d1,d2,d3,d4))
