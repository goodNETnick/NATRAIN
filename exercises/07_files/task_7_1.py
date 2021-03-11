# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0

with open('ospf.txt', 'r') as f:
    for line in f:
        prefix,adm,nh,lu,oi = line.split()[1],line.split()[2].strip('[]'),line.split()[4].strip(','),line.split()[5].strip(','),line.split()[6]
        print(f'''Prefix                {prefix}
AD/Metric             {adm}
Next-Hop              {nh}
Last update           {lu}
Outbound Interface    {oi}
'''
        )

