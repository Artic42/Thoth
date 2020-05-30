import stringCounters.py as aux

def decoder (prvLine, Line, nxtLine):
	if Line[0] == '#':
		return title (Line)

def isFirsLineList (prvFisrtCharacter, FirstCharacter):
	pass

def isLastLineList (prvFisrtCharacter, FirstCharacter):
	pass

def is
	enumLine = aux.RemoveFirstCharacters (Line, '	')[0] == '*'
	enumPrvLine = aux.RemoveFirstCharacters (prvLine, '	')[0] == '*'
	enumNxtLine = aux.RemoveFirstCharacters (nxtLine, '	')[0] == '*'
	NenumLine = aux.RemoveFirstCharacters (Line, '	')[0] == '-'
	NenumPrvLine = aux.RemoveFirstCharacters (prvLine, '	')[0] == '-'
	NenumNxtLine = aux.RemoveFirstCharacters (nxtLine, '	')[0] == '-'
	
def title (Line):
	return aux.CountFirstCharacters (Line, '#')

#  Calculate code in case of a list been detected
def list (prvLine, Line, nxtLine, enumerated, isFirst=False, isLast=False):

	prvTabs_number = aux.CountFirstCharacters (Line, '	')
	Tabs_number = aux.CountFirsCharacters (Line, '	')
	nxtTabs_number = aux.CountFirstCharacters (Line, '	')
	prvSmaller = prvTabs_number < Tabs_number
	nxtSmaller = nxtTabs_number < Tabs_number
	X = Tabs_number - nxtTab_number

	if isFirst and isLast and enumerated:
		return 181
	if isFirst and isLast and !enumerated:
		return 141
	if isFirst and !isLast and enumerated:
		return 150
	if isFirst and !isLast and !enumerated:
		return 110
	if !isFirst and isLast and enumerated:
		return 130 + X
	if !isFirst and isLast and !enumerated:
		return 170 + X
	if prvSmaller and nxtSmaller and !enumerated:
		return 140 + X
	if prvSmaller and nxtSmaller and enumerated:
		return 180 + X
	if prvSmaller and !nxtSmaller and !enumerated:
		return 110
	if prvSmaller and !nxtSmaller and enumerated:
		return 150
	if !prvSmaller and !nxtSmaller and !enumerated:
		return 120
	if !prvSmaller and !nxtSmaller and enumerated:
		return 160
	if !prvSmaller and nxtSmaller and enumerated:
		return 130 + X
	if !prvSmaller and nxtSmaller and !enumerated:
		return 170 + X

def table (prvLine, Line, nxtLine):
	pass


