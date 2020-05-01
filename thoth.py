import sys

def main(argv):
	Path=DeterminarPath (argv)
	archivo=open(Path,'r')

	Lineas=archivo.readlines()

	for Linea in Lineas:
		
	return 0

def DeterminarPath (argv):
	if argv=='':
		return input("Introducir direccion del documento")
	else:
		return argv

def CreateSection (Linea):
	return 0

def CreateSubsection (Linea):
	return 0

def CreateSubsubsection (Linea):
	return 0

def CreateList (Linea):
	return 0

def CreateEnum (Linea):
	return 0

def CreateText (Linea):
	return 0

def DeterminateLineType(Letter, Line):
	if Letter == '#':
		CreateSection(Line)
	elif Letter == '+':
		CreateSubsection(Line)
	elif Letter == '=':
		CreateSubsubsection(Line)
	elif Letter == '-':
		if ListStarted == 1:
			AddList(Line)
		else:
			CreateList(Line)
			ListStarted = 1
if __name__ == "__main__":
	main(sys.argv[1])
