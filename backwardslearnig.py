import sys
number_of_links = int(sys.stdin.readline().strip())     #read the first line of the file and store to a variable
number_of_messages = int(sys.stdin.readline().strip())  #read second line and store it

destinations = {}                                       #create an empty array to store the destinations and match them with the links


def is_hub(link):                                       #function that checks in the array for destinations with the same link, thus a hub and returns true if there are more than one destinations
    nb = 0
    for i in destinations.values():
        if i == link:
            nb += 1
    return nb > 1

for i in range(0,number_of_messages):                   #parse the lines that contain the frames and the links that they are received to
    data = sys.stdin.readline().strip().split(" ")      #split the line in two elements of an array according to "space"
    link = int(data[0])                                 #first element of the array is the link
    frame = data[1]                                     #second is the whole frame

    dest = frame[0:4]                                   #store the first 4 digits in a variable as it contains the destination
    src = frame[4:8]                                    #next 4 digits is the source

    destinations[src] = link                            #fill the destinations array with the match of each link to a src

    if dest in destinations:                            #Checking that we have the destination's match link
        if is_hub(destinations[dest]) and destinations[dest] == link:  # Checks if the desitination is a hub and the source is in the same hub
                print frame                             #Prints only the frame
        else:
            print "%s %d" % (frame, destinations[dest]) #Else it prints the frame with the destination's link number
    else:
        print "%s %s" % (frame, " ".join([str(i) for i in range(0, number_of_links) if i != link])) #If the destination does not have a match link then we broadcast to every other link
