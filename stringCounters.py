
# CountFirstCharaters
# --------------------------------------
# It counts how many times a character appears at the beginning of a line

def CountFirstCharacters (Line, Character):
	n = 0
	for letter in Line:
		if letter == Character:
			n = n + 1
		else:
			return n
