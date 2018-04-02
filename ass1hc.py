import sys
computer_address = sys.stdin.readline().strip() #store the first line tha contains the address
data = sys.stdin.readline().strip() #store the second line that contains the dat
ptr = 0 #set a pointer in order to parse the data
while ptr < len(data):  #create a while loop in order to parse multiiple frames
    dest = data[ptr:ptr+4] #store the first 4 digits in a variable as it contains the destination
    ptr+=4 #update pointer
    src = data[ptr:ptr+4] #next 4 digits is the source
    ptr+=4 #update pointer
    length=data[ptr:ptr+8] #next 8 digits are the length of the data of the whole frame
    ptr+=8 #update pointer
    length_dec = int(length,16) #transform the length in decimal
    payload = data[ptr:ptr+(length_dec-9)*2] #store the payload according to lenght_dec
    ptr+=(length_dec-9)*2 #update pointer
    checksum_msg =data[ptr:ptr+2] #store the checksum of our data
    ptr+=2 #update pointer
    message_dec = [] #initialize an array to store our payload in decimal
    message = dest + src + length + payload + checksum_msg #our whole frame
    if computer_address != dest: #checking if the destinations matching
        print "ADDRESS MISMATCH"
        sys.exit()

    for i in range(0,length_dec*2-2,2): #transform our whole frame except the checksum to decimal
        message_dec.append(int(message[i:i+2],16))

    checksum = 0
    for c in message_dec: #checksum match checking for any errors in the message according to ALP algorithm
        checksum+=c
    checksum=checksum%128
    if(checksum != int(checksum_msg,16)):
        print "ERROR"
        sys.exit()

    res=""
    for i in range(8,len(message_dec)): #printing the result after tranforming our payload to characters
        res += chr(message_dec[i])
    print "%s %s %d %s"%(dest,src,length_dec,res)
    
