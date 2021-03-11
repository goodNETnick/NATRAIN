# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

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

