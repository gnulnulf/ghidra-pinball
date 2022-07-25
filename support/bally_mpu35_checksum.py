#!/bin/env python3
import sys
import re

print('Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))

if len(sys.argv) < 2:
    print("usage: ",sys.argv[0],"<file> [allignaddress1] [allignaddress2] .." )
    exit(2)
blocksize=0x400
allignaddress=[]
if len(sys.argv) > 2:
    for a in sys.argv[2:]:
        if "0x" in a:
            allignaddress.append(int(a,16))
        else:
            allignaddress.append(int(a)) 

print(allignaddress)
fname=sys.argv[1]
f = open(fname, 'rb')
if f:
    file=f.read()
    print("file:",str(fname))
    print("size:",len(file) )

    start=0
    while start<len(file):
        checksum=0

        for i in range(blocksize):
            checksum=checksum+file[start+i]
#            print(hex(i),":",file[start+i])

        print(hex(start),"-",hex(start+blocksize-1),"checksum:",hex(checksum&0x000000ff))
        for a in allignaddress:
            if a>= start and a<start+blocksize:
                print(hex(a),"old: ",hex(file[a]),"new: " , hex(0xFF-(checksum-file[a])%256))
        start =start + blocksize

