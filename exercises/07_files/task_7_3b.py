# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
needv = int(input('wich vlan d u want? :'))
src = 'CAM_table.txt'
cams = []
with open(src, 'r') as f:
    for line in f:
        if len(line) > 1:
            if line[1].isdigit():
                vlan, mac, _, intf = line.strip().split()
                cams.append([int(vlan), mac, intf])

for elem in sorted(cams):
    if elem[0] == needv:
        print(f'''{elem[0]:<8}{elem[1]:<18}{elem[2]:<8}''')



