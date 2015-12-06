import random
from menu import mk_menu
from menu import hoofdmenu
from menu import titelbox
from toetsenbord import maak_toetsenbord
import time

def maak_oef(letters, eerste_keer=True):
	"""Hussel de letters doorelkaar, geef ze weer in groepjes van twee of groter
	met in totaal 75 karakters."""
	vraag = ''
	z = 0
	for x in xrange(75):
		# zorg dat er geen spaties zitten op de laatste of 1 na laatste letter
		# doe dit door vroegtijdig een spatie te zetten en z zo in te stellen
		# dat er daarna geen spatie meer komt
		if (x == 70 and z > 2) or (x in [71, 72, 73] and z > 1):
			vraag += ' '
			z = -3
		# doe een spatie tussen iedere 2,3,4,5 letters
		elif random.randint(1,100) < (25 * (z - 1)):
			vraag += ' '
			z = 0
		#kies een letter uit de gegeven letters
		else:
			y = random.randint(0, len(letters) - 1)
			vraag += letters[y]
			z += 1

	#zorg dat bij de eerste poging de letterrij wordt getoond 
	#waar de vraag op van toepassing is, 
	#bij latere pogingen gebeurt dit niet.
	#Met - kunnen de vragen evt. geskipt worden bij het testen.
	if eerste_keer:
		print ''
		maak_toetsenbord(letters)
	print ''

	antw = raw_input(vraag + '\n')
	if antw != vraag:
		if antw != '-':
			maak_oef(letters, eerste_keer=False)

def mk_oefeningen(num, *rijen):
	"""Zet een of meerdere rijen letters om in een serie oefeningen.
	Vervolgens wordt een menu geprint en wordt iedere oefening aangeboden."""
	if len(rijen) == 1:
		rij = rijen[0]
		combirij = [rij[:2], rij[:4], rij[:6], rij[:8], rij[8:] + rij[:2], rij[:]]
	else:
		combirij = []
		for x in xrange(10):
			combirij.append('')

		for rij in rijen:
			rij = [rij[:2], rij[2:4], rij[4:6], rij[6:8], rij[:2], rij[:4], 
				rij[:6], rij[:8], rij[8:] + rij[:2], rij[:]]
			for x in xrange(10):
				combirij[x] += rij[x]

	mk_menu('', combirij, 'submenu', num)
	for i in combirij:
		maak_oef(i)
	if num < 6:
		vraag_doorgaan(num)
	else:
		vraag_ok()

def vraag_doorgaan(num):
	print 'Wil je doorgaan met les %d of naar het [m]enu?' % (num + 1)
	print "'d' = doorgaan, 'm' = menu"
	x = None
	while x not in ['m', 'd']:
		x = raw_input('> ').lower()
		if x == 'd':
			mk_oefeningen(num + 1, *hoofdmenu[num][1])
		elif x == 'm':
			typcursus()

def vraag_ok(prompt='Wil je doorgaan? (j/n)\n', pogingen=5):
	for p in xrange(pogingen):
		ok = raw_input(prompt)
		if ok in ['j', 'ja', 'J', 'JA']:
			return True
		elif ok in ['n', 'nee', 'N', 'NEE']:
			break
		else:
			if p == 0:
				prompt = "Typ 'j' of 'n'"
			else:
				prompt = ''
	
	print 'Het programma wordt afgesloten.'
	exit(0)

def maak_een_keuze(prompt='Oefening: '):
	"""Vraagt de gebruiker om input. Als de input omgezet kan worden in een
	integer dan geeft de functie een integer terug, anders alleen tekst."""
	keuze = raw_input(prompt)
	try:
		return int(keuze)
	except:
		return keuze

def typcursus(doorgaan=True, pogingen_t=3):
	"""Biedt de gebruiker een menu aan met een aantal keuzes.
	De gebruiker krijgt een aantal pogingen om geldige invoer te geven.
	Lukt dat niet dan krijgt hij de vraag of hij door wil gaan."""
	while doorgaan == True:
		mk_menu('Welke oefening wil je doen?', hoofdmenu, 'lang')

		p = pogingen_t
		prompt = 'Oefening: '
		while p >= 0:
			keuze = maak_een_keuze(prompt)
			if not isinstance(keuze, int):
				p -= 1
				if p == 0:
					if vraag_ok() == True:
						p = 1
						prompt = 'Typ een getal tussen de 1 en 6: '
					else:
						doorgaan = False
						break
				elif p == pogingen_t - 1:
					prompt = 'Typ een getal tussen de 1 en 6: '
				else:
					prompt = ''
			else:
				k = hoofdmenu[keuze - 1][1]
				mk_oefeningen(keuze, *k)
				break

titelbox("LEER TYPEN MET 10 VINGERS...", "Het doel van deze cursus is om met tien vingers te leren typen.",
	"Leer stukje voor stukje de rijen van je toetsenbord kennen.",
	"Leg je wijsvingers op de F en de J en typ de rij met letters na.",
	"Kies daarvoor eerst een rij waarmee je wil beginnen, bijvoorbeeld 1.", "",
	"TIP: Als je een foutje maakt: druk dan op ENTER en niet op BACKSPACE,",
	"dan kan je namelijk nogmaals dezelfde oefening doen.")

typcursus()
