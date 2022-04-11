outFile = open("output.txt", "w")

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b,
    '**': lambda a, b: a ** b
}	

res = ''

with open("input_file.txt") as inFile:

	for line in inFile:
		s = line.split()
		a = int(s[1])
		b = int(s[2])
		res += str(operators[s[0]](a, b)) + ','
	
	outFile.write(res[:-1])
