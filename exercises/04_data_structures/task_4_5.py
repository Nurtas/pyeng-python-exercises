# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

# ip_1 = command1[30:39:2]
# ip_2 = command2[30:38:2]
# result = sorted(set(ip_1).intersection(ip_2))
# print(result)

ip_1 = command1[-9:].split(',')
ip_2 = command2[-7:].split(',')

result = sorted(set(ip_1).intersection(ip_2))
print(result)
