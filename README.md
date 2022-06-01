# Simple_IPV4
A simple package for calculating IPV4 info


Usage:

	from ipv4info import Ip4

	ip = Ip4("192.168.88.67/26")
  
	mask_num = ip.mask_binary()   # Binary mask
	mask_dec = ip.mask_decimal()  # Decimal mask
