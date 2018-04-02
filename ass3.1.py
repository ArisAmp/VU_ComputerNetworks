# coding=utf-8
#Exploration Assignment 3

#1. The difference is that the first routing table is a Persistent routing table while the second routing table is an Active routing table.
#   The persistent one is associated to IPv4 while the active one is associated to Internet 6. The difference between a persistent an active routing table is in the name;
#   a persistent routing table is a routing table that has established connections and that doesn’t change while an active routing table change often.

#2. On macOS, the first column header corresponds to both the Network Destination and the Subnet Mask.
#   The second column header corresponds to the Gateway.

#3. Network Destination & Subnet Mask – Destination on mac.
#   Gateway –  Gateway.
#   255.255.0.0 as a subnet mask is equivalent to 11111111 11111111 00000000 00000000 In binary.
#   255.255.0.0 as a subnet mask would also have a network prefix of /16 This is means that the network prefix would be 8 bits or rather in binary, 11111111 11111111 00000000 00000000.
#   This is why 255.255.0.0 can also written 145.94.162.184/16.




import sys


def is_in_subnet(net_ip, mask, ip):
    return (net_ip & mask) == (ip & mask)


def subnet_size(mask):
    return ~mask & 0xffffffff

ip2int = lambda ip: reduce(lambda a, b: (a << 8) + b, map(int, ip.split('.')), 0)
int2ip = lambda n: '.'.join([str(n >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])

(nb_subnet, nb_ip) = sys.stdin.readline().strip().split(" ")
nb_subnet = int(nb_subnet)
nb_ip = int(nb_ip)

subnets = []
for i in range(0, nb_subnet):
    subnet = sys.stdin.readline().strip().split(" ")
    subnets.append([ip2int(subnet[0]), ip2int(subnet[1]), ip2int(subnet[2])])

for i in range(0, nb_ip):
    ip = ip2int(sys.stdin.readline().strip())
    min_size = 0
    found_subnet = False
    biggest_subnet = None
    for subnet in subnets:
        if is_in_subnet(subnet[0], subnet[1], ip):
            if subnet_size(subnet[1]) <= min_size or not found_subnet:
                min_size = subnet_size(subnet[1])
                biggest_subnet = subnet
                found_subnet = True
    if subnet is not None:
        print int2ip(biggest_subnet[2])