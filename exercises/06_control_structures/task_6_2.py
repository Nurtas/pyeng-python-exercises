# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

stop = False

while not stop:
   ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')

   if ip_address == 'exit':
      stop = True
      continue

   ip = ip_address.split('.')

   for i in range(0, len(ip)):
      ip[i] = int(ip[i])

   # 'unicast' - если первый байт в диапазоне 1-223
   if ip[0] >= 1 and ip[0] <= 223:
      print(f'unicast - {ip[0]}')
   # 'multicast' - если первый байт в диапазоне 224-239
   elif ip[0] >= 224 and ip[0] <= 239:
      print(f'multicast - {ip[0]}')
   # 'local broadcast' - если IP-адрес равен 255.255.255.255
   elif ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255: 
      print(f'local broadcast - если IP-адрес равен {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
   # 'unassigned' - если IP-адрес равен 0.0.0.0
   elif ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0: 
      print(f'local broadcast - если IP-адрес равен {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
   else:
      # 'unused' - во всех остальных случаях
      print("'unused' - во всех остальных случаях")
else:
   print('Program exit...')
