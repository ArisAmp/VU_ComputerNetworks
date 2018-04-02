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
