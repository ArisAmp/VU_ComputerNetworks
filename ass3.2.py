import sys
from collections import defaultdict


addr = raw_input()
nb = int(raw_input())
routing = defaultdict(lambda: {})


def update_routing(addr, source, delay):
    routing[addr][source] = delay
    routing[source][addr] = delay


def do_routing(src, dest):
    min_delay = sys.maxint
    min_neighbour = None
    for neighbour in routing:
        if dest in routing[neighbour]:
            delay = routing[neighbour][dest]
            if delay <= min_delay:
                min_neighbour = neighbour
                min_delay = delay
    if min_neighbour == addr:
        min_neighbour = dest
    return min_neighbour, min_delay


for i in range(0, nb):
    line = raw_input().split(" ")
    if line[0] == 'R':
        source = line[1]
        delay_temp = int(line[2])
        nb_entries = int(line[3])
        update_routing(addr, source, delay_temp)
        for i in range(4, 4 + nb_entries * 2, 2):
            router = line[i]
            if router != addr:
                delay = int(line[i + 1]) + delay_temp
            else:
                delay = int(line[i + 1])
            update_routing(source, router, delay)
        print "THANK YOU"

    else:
        source = line[1]
        destination = line[2]
        message = " ".join(line[3:len(line) - 1])

        (n, d) = do_routing(source, destination)
        if n is not None:
            print n + " " + str(d)
        else:
            print "NO ROUTE"