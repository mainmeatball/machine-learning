outFile = open("output.txt", "w")
inFile1 = open("input1.txt", "r")

res = ''

with open("input2.txt") as inFile2:

	for line2 in inFile2:
		
		s = line2.rstrip('\n').split()
		start = int(s[0])
		end = int(s[1]) + 1

		line1 = inFile1.readline()

		res += line1[start:end] + ' '

outFile.write(res[:-1])

outFile.close()
inFile1.close()