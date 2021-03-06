import stringCounters as aux

def decoder (prvLine, Line, nxtLine):
	prvFC = FirstCharacter (prvLine)
	FC = FirstCharacter (Line)
	nxtFC = FirstCharacter (nxtLine)

	if FC == '#':
		return title (Line)

	if FC == '*' or FC == '-':
		return list (prvLine, 
					Line,
					nxtLine,
					isEnumerated(FC),
					isFirst = isFirsLineList(FC, nxtFC),
					isLast = isLastLineList(prvFC, FC))

# Calculate code in case of a title of a section
def title (Line):
	return aux.CountFirstCharacters (Line, '#')

#  Calculate code in case of a list been detected
def listLastStep (prvLine, Line, nxtLine, enumerated, isFirst=False, isLast=False):
	prvTabs_number = aux.CountFirstCharacters (Line, '	')
	Tabs_number = aux.CountFirsCharacters (Line, '	')
	nxtTabs_number = aux.CountFirstCharacters (Line, '	')
	prvSmaller = prvTabs_number < Tabs_number
	nxtSmaller = nxtTabs_number < Tabs_number
	X = Tabs_number - nxtTab_number

	if isFirst and isLast and enumerated:
		return 181
	if isFirst and isLast and not enumerated:
		return 141
	if isFirst and not isLast and enumerated:
		return 150
	if isFirst and not isLast and not enumerated:
		return 110
	if not isFirst and isLast and enumerated:
		return 130 + X
	if not isFirst and isLast and not enumerated:
		return 170 + X
	if prvSmaller and nxtSmaller and not enumerated:
		return 140 + X
	if prvSmaller and nxtSmaller and enumerated:
		return 180 + X
	if prvSmaller and not nxtSmaller and not enumerated:
		return 110
	if prvSmaller and not nxtSmaller and enumerated:
		return 150
	if not prvSmaller and not nxtSmaller and not enumerated:
		return 120
	if not prvSmaller and not nxtSmaller and enumerated:
		return 160
	if not prvSmaller and nxtSmaller and enumerated:
		return 130 + X
	if not prvSmaller and nxtSmaller and not enumerated:
		return 170 + X

# Return first non tab character of a line
def FirstCharacter (Line):
	
	return aux.RemoveFirstCharacters (Line, '	')[0]

def isFirsLineList (prvFirstCharacter, FirstCharacter):
	prvLineList = prvFirstCharacter == '*' or prvFirstCharacter == '-'
	LineList = FirstCharacter == '*' or FirstCharacter == '-'
	SameTypeList = FirstCharacter == prvFirstCharacter
	return not prvLineList and LineList or not SameTypeList

def isLastLineList (FirstCharacter, nxtFirstCharacter):
	nxtLineList = nxtFirstCharacter == '*' or nxtFirstCharacter == '-'
	LineList = FirstCharacter == '*' or FirstCharacter == '-'
	SameTypeList = FirstCharacter == nxtFirstCharacter
	return not nxtLineList and LineList or not SameTypeList

def isEnumerated (FirstCharacter):
	return FirstCharacter == '*'

# Calculate codes in case of a table
def table (prvLine, Line, nxtLine):
	pass


