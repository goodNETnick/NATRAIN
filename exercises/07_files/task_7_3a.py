# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт:  Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

src = 'CAM_table.txt'
cams = []
with open(src, 'r') as f:
    for line in f:
        if len(line) > 1:
            if line[1].isdigit():
                vlan, mac, _, intf = line.strip().split()
                cams.append([int(vlan), mac, intf])
for elem in sorted(cams):
    print(f'''{elem[0]:<8}{elem[1]:<18}{elem[2]:<8}''')



