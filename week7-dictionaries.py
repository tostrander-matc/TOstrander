#!/usr/bin/env python
#Dictionary entries================================
IpDictionary = {"server1.testlab.com":"192.168.1.10"}
IpDictionary["server2.testlab.com"] = "192.168.1.12"
IpDictionary["server3.testlab.com"] = "192.168.1.13"
IpDictionary["server4.testlab.com"] = "192.168.1.14"
IpDictionary["server5.testlab.com"] = "192.168.1.15"
IpDictionary["server6.testlab.com"] = "192.168.1.16"

#FQDNs===============================================
print("FQDNs are: ", IpDictionary.keys())
print("\n")
#VALUES - IP ADDRESSES ================================
print("IP Addresses: ", IpDictionary.values())
print("\n")

#FULL RECORDS (KEYS AND VALUES)========================
print("Dictionary contents: ", IpDictionary.items())
print("\n")

#NEW ENTRIES (KEYS AND VALUES)========================
IpDictionary["server7.testlab.com"] = "192.168.1.16"
IpDictionary["server8.testlab.com"] = "192.168.1.17"

#TEST 1==============================================
key = 'server2.testlab.com'
if key in IpDictionary:
	print('Yes, {} is in the dictionary.'.format(key))
	print("\n")
else:
	print('No, {} is not in the dictionary.'.format(key))

#TEST 2===============================================
key1 = 'server10.testlab.com'
if key1 in IpDictionary:
	print('Yes, {} is in the dictionary.'.format(key1))
else:
	print('No, {} is not in the dictionary.'.format(key1))
