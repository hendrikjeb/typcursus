# -*- coding: utf-8 -*-
# In dit bestand wordt een toetsenbord gemaakt, dat wat betreft de te oefenen
# letters alleen de letters laat zien die op dat moment worden geoefend.

functie_rij = ['ESC', 'F1',	'F2', 'F3',	'F4', 'F5', 'F6', 'F7',	'F8', 'F9',	
		'F10', 'F11', 'F12', 'BREAK', 'PRTSCR', 'DEL']
	
getallenrij = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', 
	'=', 'BACKSPACE']

qwerty_rij = ['TAB   ', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 
	'[', ']', '    \\ ']

asdf_rij = ['CAPSLOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 
	'\'', '    ENTER']

zxcvbnm_rij = ['SHIFT      ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', 
	'/', '      SHIFT']

spatie_rij = ['CTRL   ', 'WIN', 'ALT', 	'                                 ', 
	'ALT GR', 'MENU', '  CTRL']

toetsenbordrijen = [getallenrij, qwerty_rij, asdf_rij, zxcvbnm_rij, spatie_rij]

def maak_toetsenrij(toetsenrij, letters):
	"""Deze functie maakt een rij toetsen. Wat betreft toetsen met lengte 1, 
	
		wordt gekeken of de toets voorkomt in de opgegeven letterrij. 
		Is dat niet het geval, dan maakt hij een lege toets."""
	toetsen = [ '', '', '' ]
	
	#stel een tekenreeks samen met bovenkanten, middens en onderkanten van toetsen.
	for toets in toetsenrij:
		#kijk voor toetsen met lengte één of ze voorkomen in de opgegeven letterrij.
		if len(toets) == 1:
			if toets not in letters[:]:
				toets = ''
		#maak kleine toetsen lang genoeg
		if len(toets) < 3:
			lengte = 3
		else:
			lengte = len(toets)

		#voeg voor iedere toets een bovenkant, midden en onderkant toe
		toetsen[0] += u"{0}{1}{2}".format(u'\u250c', 
			lengte * u'\u2500', u'\u2510')
		toetsen[1] += u"{0}{1:^{lengte}s}{0}".format(u'\u2502', 
			toets, lengte=lengte)
		toetsen[2] += u"{0}{1}{2}".format(u'\u2514', 
			lengte * u'\u2500', u'\u2518')

	# print de drie zojuist samengestelde tekenreeksen
	for t in toetsen:
		print t

def maak_toetsenbord(letters='qwertyuiop[]asdfghjkl;\'zxcvbnm,./', 
	rij=toetsenbordrijen):
	letters = letters.upper()

	maak_toetsenrij(rij[0], rij[0])
	maak_toetsenrij(rij[1], letters)
	maak_toetsenrij(rij[2], letters)
	maak_toetsenrij(rij[3], letters)
	maak_toetsenrij(rij[4], rij[4])