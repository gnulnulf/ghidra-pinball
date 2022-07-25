
import sys
import re

# build an array which describes how far away each character is from the next
def getDifferences(x):
    ccount=[]
    for i in range(0,len(x) - 1):
        ccount.append( ord(x[i+1]) - ord(x[i]))
    return ccount

# make sure we have the correct number of arguments
try:
    # get the search string and the difference array of the search string
    srch=sys.argv[1]
    c=getDifferences(srch)
    print(c)
    
except IndexError:
    sys.stdout.write("usage: %s\"search string\" file...\n" % sys.argv[0]) 
    sys.exit(-1)




for fname in sys.argv[2:]:
    with open(fname, 'rb') as f:
        data = f.read()

    matches = []  # initializes the list for the matches
    curpos = 0  # current search position (starts at beginning)
    pattern = re.compile( srch.encode('raw_unicode_escape'))  # the pattern to search

    while True:
        m = pattern.search(data[curpos:])  # search next occurence
        if m is None: break  # no more could be found: exit loop
        matches.append(curpos + m.start() )
        curpos += m.end()  # next search will start after the end of found string

    for match in matches:
        print(format(match, '04X'))

    #print(print(z.encode('hex')))
#    print("looking for %s in %s" % (s, fname) )
#    print("File length %s" % (len(f)))
    # loop through the file checking if each character is the begging of a pattern
    # that matches the difference values
 #   for i in range(0,len(f) - len(s)):
  #      x=getDifferences( str( f[i:i+len(s)] )  )
   #     if x == c:
    #        print("\tmatch in %s at offset 0x%2x" % (fname,i) )
