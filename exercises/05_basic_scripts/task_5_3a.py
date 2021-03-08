# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

#input("Введите режим работы интерфейса (access/trunk): ")
#input("Введите тип и номер интерфейса: ")
#input("Введите номер влан(ов): ")
mode = "access"
intf = "Fast0/0/0"
vlanprompt = {'access':'Введите номер VLAN:', 'trunk':'Введите разрешенные VLANы:'}

vlans = input(vlanprompt[mode])

choose = {'trunk':trunk_template, 'access':access_template}

print('interface ' + intf)
templ = '  ' + '\n  '.join(choose[mode])
print(templ.format(vlans))
