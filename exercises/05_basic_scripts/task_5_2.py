# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip,mask = input('ввод IP-сети в формате: 10.1.1.0/24: ').split('/')
d1,d2,d3,d4 = ip.split('.')
bmask = '1' * int(mask) + '0'*int(mask)
bm1,bm2,bm3,bm4 = bmask[0:8],bmask[8:16],bmask[16:24],bmask[24:32]

templ = f'''Network:
{d1:<8}  {d2:<8}  {d3:<8}  {d4:<8}
{int(d1):>08b}  {int(d2):>08b}  {int(d3):>08b}  {int(d4):>08b}

Mask:
/{mask}
{int(bm1, 2):<8}  {int(bm2, 2):<8}  {int(bm3, 2):<8}  {int(bm4, 2):<8}
{bm1:>08}  {bm2:>08}  {bm3:>08}  {bm4:>08}'''

print(templ)
