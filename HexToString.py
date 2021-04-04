import re
from HID_PID_Definitions import *
import argparse

UsagePage=None
def itemByHex(hexd):
	for items in HID_Items:
		for item in items:
			hItem=items[item]
			if (hItem == (hexd & 0xFC)):
				return [item,hexd & 0b11]
	raise Exception('item error')
def valueByHex(item, len, hexd):
	constants = ConstByItem[item]
	changePage = False
	if item=='Usage':
		if len == 4:
			tempUsagePage = valueByHex('Usage_Page', 1, hexd>>16)
			hexd = hexd & 0x0000FFFF
			constants = UsageByPage[tempUsagePage]
			changePage = True
		else:
			constants = UsageByPage[UsagePage]
	for key in constants:
		if constants[key]==hexd:
			val = key
			if changePage:
				val += ':'+tempUsagePage
			return val
	if constants != {}:
		print(item, hex(hexd))
		print('value constant missing')
	if len==0:
		return ''

	if hexd > (1<<len*8-1)-1: #calculate complement
		hexd = (1<<(len*8)) - hexd
		hexd = -hexd
		return hexd
	return hexd

parser = argparse.ArgumentParser(description="Decode an HID descriptor sequence and generate a human readable structure")
parser.add_argument('-i', '--input', dest='fileIn', action='store', help='Input file name')
parser.add_argument('-o', '--output', dest="fileOut", action='store', help='Output file name')
args = parser.parse_args()

fileIn = "Hex.txt"
fileOut = ""
if(args.fileIn):
	fileIn = args.fileIn
if(not args.fileOut):
	fileOut = open("Out.rptDsc",'w')
else:
	fileOut = open(args.fileOut,'w')

lines  = open(fileIn).readlines()
tabcnt = 0
for line in lines:
	# print('------',line) #echo
	line=line.expandtabs(tabsize=4)
	key=line
	pos=line.find('//') #remove comments
	if pos>=0:
		key=line[:pos]
	hexes = re.findall('0x[0-9A-Fa-f]*',key)
	if hexes==[]:
		continue

	item,length=itemByHex(int(hexes[0],16)) #got item
	if length==3: #0b11 represents 4-byte value
		length=4

	hValue=0
	for i in range(0,length):
		hValue += int(hexes[1+i],16)<<(i*8) #multi byte value
	# print(str(item)+", "+str(length)+", "+str(hValue))
	value=valueByHex(item, length, hValue) #got value

	if item=='Usage_Page':
		UsagePage=value #update UsagePage
	if item == 'End_Collection':
		tabcnt-=1
	for i in range(0,tabcnt):
		fileOut.write('	');
	fileOut.write(item+'('+str(value)+'),\n')
	if item == 'Collection':
		tabcnt+=1
fileOut.close()
