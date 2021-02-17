# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

stop = False

while not stop:
   ip_address = input('Введите IP-адреса в формате 10.0.1.1: ')

   if ip_address == 'exit':
      stop = True
      continue

   ip = ip_address.split('.')

   if ip[0].isalpha() or ip[1].isalpha() or ip[2].isalpha() or ip[3].isalpha():
      print('Введите IP адрес заново... \n')
      continue

   for i in range(0, len(ip)):
      ip[i] = int(ip[i])

   # 'unicast' - если первый байт в диапазоне 1-223
   if ip[0] >= 1 and ip[0] <= 223:
      print(f'unicast - {ip[0]}')
      stop = True
      continue
   # 'multicast' - если первый байт в диапазоне 224-239
   elif ip[0] >= 224 and ip[0] <= 239:
      print(f'multicast - {ip[0]}')
      stop = True
      continue
   # 'local broadcast' - если IP-адрес равен 255.255.255.255
   elif ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255: 
      print(f'local broadcast - если IP-адрес равен {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
      stop = True
      continue
   # 'unassigned' - если IP-адрес равен 0.0.0.0
   elif ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0: 
      print(f'local broadcast - если IP-адрес равен {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
      stop = True
      continue
   else:
      # 'unused' - во всех остальных случаях
      print("'unused' - во всех остальных случаях")
else:
   print('Program exit...')