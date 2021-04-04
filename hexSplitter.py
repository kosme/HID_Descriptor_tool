import argparse
word_size = 2

parser = argparse.ArgumentParser(description="Analyze a dumped HID descriptor and give it format for decription")
parser.add_argument('-i', '--input', dest='fileIn', action='store', help='Input file name')
parser.add_argument('-o', '--output', dest="fileOut", action='store', help='Output file name')
args = parser.parse_args()

fileIn = "DscInput.rptDsc"
fileOut =  ""
if(args.fileIn):
	fileIn = args.fileIn
if(not args.fileOut):
	f_out = open("Hex.out",'w')
else:
	f_out = open(args.fileOut,'w')

f_in = open(fileIn,'r')

commas = True
f_in.seek(word_size)
c = f_in.read(1)
if(c is ','):
    commas = True
else:
    commas = False
f_in.seek(0) #Goto begginning of File
c=f_in.read(word_size)

while(c):
    line=[]
    if not commas:
        f_in.read(1)
    else:
        f_in.read(2)
    last=-1
    try:
        if(int(c[-1]) is 0):
            last = -1
        else:
            last = int(c[-1])%2
    except ValueError:
        if(c[-1]=='a' or c[-1]=='c' or c[-1]=='e'):
            last = 0
        else:
            last = 1
    if(word_size is 2):
        c="0x"+c
    line.append(c)
    if(last>-1):
        c=f_in.read(word_size)
        if not commas:
            f_in.read(1)
        else:
            f_in.read(2)
        if(word_size is 2):
            c="0x"+c
        line.append(c)
    if last == 0:
        c=f_in.read(word_size)
        if not commas:
            f_in.read(1)
        else:
            f_in.read(2)
        if(word_size is 2):
            c="0x"+c
        line.append(c)
    s=""
    for l in line:
        s+=l+", "
    f_out.write(s+"\n")
    c=f_in.read(word_size)

f_out.close()
f_in.close()
