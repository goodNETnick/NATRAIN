# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

src = argv[1]
dest = argv[2]
with open(src, 'r') as f, open(dest, 'w') as d:
    for line in f:
        words = line.split()
#        if set(words) & set(ignore):
        if words[0] in ignore:
            pass
        elif line.startswith('!'):
            pass
        else:
            d.write(line)
            print(line.strip())

