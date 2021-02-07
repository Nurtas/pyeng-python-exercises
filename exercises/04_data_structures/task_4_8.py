# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = "192.168.3.1"

# a = int(ip[:3])
# b = int(ip[4:7])
# c = int(ip[8:9])
# d = int(ip[10:11])

# bin_a = format(a, '08b')
# bin_b = format(b, '08b')
# bin_c = format(c, '08b')
# bin_d = format(d, '08b')

# print(
#   f"""
#   {a}       {b}       {c}         {d}
#    {bin_a}  {bin_b}  {bin_c}  {bin_d}
#   """
# )
ip = ip.split('.')

a = int(ip[0])
b = int(ip[1])
c = int(ip[2])
d = int(ip[3])

# .format()
ip_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(ip_template.format(a,b,c,d))

# f-строки 
print(f'''
{a:<8}  {b:<8}  {c:<8}  {d:<8}
{a:08b}  {b:08b}  {c:08b}  {d:08b}
''')