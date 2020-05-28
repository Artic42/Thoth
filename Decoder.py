import stringCounters.py as aux

def decoder (prvLine, Line, nxtLine):
	pass

def titte (Line):
	Head = Line[:5]
	return aux.CountFirstCharacters (Line, '#')


def list (prvLine, Line, nxtLine, enumerated, isFirst=False, isLast=False):
	if isFirst and isLast and enumerated:
		return 181
	if isFirst and isLast and !enumerated:
		return 141

	prvTabs_number = aux.CountFirstCharacters (Line, '	')
	Tabs_number = aux.CountFirsCharacters (Line, '	')
	nxtTabs_number = aux.CountFirstCharacters (Line, '	')
	prvSmaller = prvTabs_number < Tabs_number
	nxtSmaller = nxtTabs_number < Tabs_number
	X = Tabs_number - nxtTab_number

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


