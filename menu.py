# De letterrijen
asdf = 'fjdksla;gh'
qwer = 'rueiwoqpty'
zxcv = 'vncmx,z.b'

# Hiermee geven we de menu-items een nummer
hoofdmenu = [
	['Middelste rij', [asdf]],
	['Bovenste rij ', [qwer]],
	['Middelste en bovenste rij', [asdf, qwer]],
	['Onderste rij ', [zxcv]],
	['Middelste en onderste rij', [asdf, zxcv]],
	['Bovenste, middelste en onderste rij', [qwer, asdf, zxcv]]
	]

def titelbox(titel, *ondertitels):
	"""Zet een box om de titel heen."""
	
	min_breedte = len(titel) + 2

	for regel in ondertitels:
		if len(regel) > (min_breedte - 2):
			min_breedte = len(regel) + 2

	if titel != '':
		print '\n' + titel.center(min_breedte)
	print u"\u250c" + min_breedte * u"\u2500" + u"\u2510"
	for regel in ondertitels:
		print u"\u2502", regel.ljust(min_breedte - 2), u"\u2502"
	print u"\u2514" + min_breedte * u"\u2500" + u"\u2518"


def mk_menu(titel='', menu=hoofdmenu, smaak='kort', num=0):
	"""Maak een lijstje met menu-items."""
	menulijst = []
	aant = len(menu)

	for i in xrange(aant):
		if smaak == 'lang':
			menulijst.append('%d. %s' % (i + 1, menu[i][0]))
			menulijst.append('   [%s]' % (', '.join(menu[i][1])))
			if i == aant - 1:
				break
			menulijst.append('')
		
		elif smaak == 'breed':
			menulijst.append('%d. %s (%s)' % (i + 1, menu[i][0], 
				', '.join(menu[i][1])))

		elif smaak == 'submenu':
			menulijst.append('%d%s. %s' % (num, chr(ord('a')+i), menu[i]))			
		
		else:
			menulijst.append('%d. %s' % (i + 1, menu[i][0]))
			#als er 1 letterrij is, geef dan de letters van de rij
			if len(menu[i][1]) == 1:
				menulijst[i] += ' (%s)' % menu[i][1][0]

	return titelbox(titel, *menulijst)