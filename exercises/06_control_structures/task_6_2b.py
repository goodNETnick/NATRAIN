# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = []
ipcheck = ''
while not ip:
   ip = input('ввод IP-адреса в формате 10.0.1.1: ').split('.')
   ip1 = int(ip[0])
   if len(ip) != 4:
      ipcheck = 'bad'
   for elem in ip:
      if not elem.isdigit() or int(elem) < 0 or int(elem) >255:
         ipcheck = 'bad'
   if ipcheck == 'bad':
      ip = []
      print('bad')
   ipcheck = ''

if ip == '0.0.0.0':
   print('unassigned')
elif ip == '255.255.255.255':
   print('local broadcast')
elif ip1 > 0 and ip1 < 224:
   print('unicast')
elif ip1 > 223 and ip1 < 240:
   print('multicast')
else:
   print('unused')

