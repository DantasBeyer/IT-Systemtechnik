# Der Benutzer soll zwei Zahlen in das Programm eingeben, danach soll er entscheiden, ob die Zahlen addiert,
# subtrahiert, multipliziert oder dividiert werden, diese Entscheidung soll über die Eingabe der folgenden
# Symbole getätigt werden:
# Bei der Division durch 0 soll die Ausgabe "Das kann nur Chuck Norris" erfolgen
# Nach der Auswahl soll das Ergebnis der Rechnung ausgegeben werden,
# bzw. eine Fehlermeldung, falls eine
# falsche Auswahl getroffen wurde.

# zahl1 = int(input("Zahl 1 :"))
# operator = input("Rechenart +, -, *, /")
# zahl2 = int(input("Zahl 2 :"))

# if operator == "+":
#     solution = zahl1 + zahl2
#     print(solution)
# elif operator == "-":
# 	solution = zahl1 - zahl2
# 	print(solution)
# elif operator == "*":
# 	solution = zahl1 * zahl2
# 	print(solution)
  
# elif operator == "/":
#     if zahl2 == 0:
#         print("Das kann nur Chuck Norris")
#     else:
#     	solution = zahl1 / zahl2
# print(solution)



# Nach dem Ohmschen Gesetz berechnet sich der Widerstand eines ohmschen Widerstandes mit:
# U = R * I
# R = U/I
# I = U/R
# Schreiben Sie ein Programm, in das der Benutzer zunächst über die Eingabe der Buchstaben R, U oder I
# auswählen kann, welche Größe berechnet werden soll. Gibt er einen falschen Buchstaben ein, soll eine Meldung
# über die Fehleingabe erfolgen.
# Anschließend soll er die Werte der fehlenden Größen eingeben. Am Ende gibt das Programm den Wert der
# gesuchten Größe mit der richtigen Einheit aus


#?Das ohmsche Gesetz dient zur Berechnung des Verhältnisses zwischen Spannung, Strom und Widerstand in einem Stromkreis! 
#spannung: U = "R" * "I", stärke: I = "U" / "R", wiederstand: R = "U" / "I"


# u_r_i = input("gibt ein wert ein U, R oder I: ").upper()
    
# if u_r_i == "U":
# 	r = float(input("gibt ein wert für R ein: "))
# 	i = float(input("gibt ein wert für I ein: "))
# 	print("Die Spannung ist ", r*i, "Volt" )
# elif u_r_i == "I":
# 	u = float(input("gibt ein wert für U ein: "))
# 	r = float(input("gibt ein wert für R ein: "))
# 	print("Die Stärke ist ", u/r, "Ohm")
# elif u_r_i == "R":
#     u = float(input("gibt ein wert für U ein: "))
#     i = float(input("gibt ein wert für I ein: "))
#     print("Der Wiederstang ist ", u/i, "Ampere")
# else:
# 	print("falsche eingabe, bitte U, R oder I eingeben ")




# Ein Hardware-Großhändler führt ein Rabattsystem für Stammkunden ein: Liegt der Bestellwert zwischen 0 und
# 100 €, erhält der Kunde einen Rabatt von 10 %. Liegt der Bestellwert höher, aber insgesamt nicht über 500 €,
# beträgt der Rabatt 15 %, in allen anderen Fällen beträgt der Rabatt 20 %. Nach Eingabe des Bestellwertes soll
# der ermäßigte Bestellwert berechnet und ausgegeben werden.


promotion_1  = 10
promotion_2 = 15
promotion_3 = 20
  




# Der BMI berechnet sich aus dem Körpergewicht [kg] dividiert durch das Quadrat der Körpergröße [m2
# Die Formel lautet: BMI = (Körpergewicht in kg): (Körpergröße in m)**2
# Der BMI einer Person wird nach den
# folgenden Regeln klassifiziert (nach DGE, Ernährungsbericht 1992):
# Klassifikation m w
# Untergewicht < 20 < 19
# Normalgewicht 20-25 19-24
# Übergewicht 25-30 24-30
# Adipositas 30-40 30-40
# massive Adipositas > 40 > 40
# Das Programm soll vom Benutzer das Gewicht [in kg] die Größe [in cm] und das Geschlecht [m/w] abfragen. Am
# Ende des Programms soll die BMI-Klassifikation der Person ausgegeben werden.


# Schaltjahres-Berechnung
# Eingabe eines Jahres -> Ausgabe Schaltjahr, kein Schaltjahr
# Laut Kalender hat ein Jahr 365 Tage. Die Erde braucht aber 365 Tage, 5 Stunden, 48 Minuten und 45 Sekunden, um die Sonne zu umrunden. Der Schalttag gleicht diese Differenz aus – allerdings nicht ganz, dazu sind die Zahlen zu unrund. Denn die überzähligen Stunden, Minuten und Sekunden addieren sich nach vier Jahren zu etwa 23 Stunden und 11 Minuten – also keinem ganzen Tag.
# Im Jahr 1582 veranlasste Papst Gregor eine Kalenderreform. Seitdem gilt der Gregorianische Kalender mit den folgenden Regeln zur Schaltjahresberechnung:
#
#
#
# Bedingung 1:
# Ist eine Jahreszahl ganzzahlig durch 4 teilbar, dann ist das Jahr ein Schaltjahr. Testwerte: 1720, 1972 und 1980 waren Schaltjahre.
# Bedingung 2:
# Ausnahme zu den Jahreszahlen, die der Bedingung 1 genügen, sind alle Jahreszahlen, die nach Bedingung 1 ein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 100 teilbar ist.
# Testwerte: 1700, 1800 und 1900 oder ferner 2100 sind keine Schaltjahre.
# Bedingung 3:
# Ausnahme zu den Jahreszahlen, die der Bedingung 2 genügen, sind alle Jahreszahlen, die nach Bedingung 2 kein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 400 teilbar.
# Testwerte: 1600 und 2000 waren Schaltjahre.
#1980 2100 1200
#jahr = int(input('Bitte gebe ein Jahr an\n'))

#if jahr % 4 == 0:


	#if jahr % 100 == 0:


		#if jahr % 400 == 0:
			#print('Schaltjahr')
		#else:
			#print('Kein Schaltjahr')
	#else:
		#print('Schaltjahr')
#else:
	#print('Kein Schaltjahr')



