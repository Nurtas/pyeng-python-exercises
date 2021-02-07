# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

# prefix             = ospf_route[6:18]
# ad_metric          = ospf_route[20:26]
# next_hop           = ospf_route[32:41]
# last_update        = ospf_route[43:48]
# outbound_interface = ospf_route[50:]
result = ospf_route.split()

print(f"""
  Prefix                {result[0]}
  AD/Metric             {result[1].strip('[]')}
  Next-Hop              {result[3].strip(',')}
  Last update           {result[4].strip(',')}
  Outbound Interface    {result[5]}
  """
)