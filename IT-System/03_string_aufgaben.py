# Erstelle einen Variable my_var und weise ihr den wert "Hallo Welt" zu
my_var = "Hallo Welt"
print (my_var)
# Erstelle eine Variable erster und weise ihr den Ersten Buchstaben des Strings my_var zu
erster = my_var[0]
print (erster)
# Erstelle eine Variable letzter und weise ihr den letzten Buchstaben des Strings my_var zu
lezter = my_var[-1]
print (lezter)
# Schneide aus dem String in my_var das Wort Hallo aus und weise es der Variable hallo zu.
hallo = my_var.split(" ")[0]
print (hallo)
# Schneide aus dem String in my_var das Wort Welt aus und weise es der Variable welt zu.
welt = my_var.split(" ")[1]
print (welt)
# Tausche den Wert der Variablen hallo und welt
hallo, welt = welt, hallo
print (hallo, welt)

a = "abcdefghijklmnopqrstuvwxyz "

# Erstelle eine Variable name und weise ihr den Vor- und Nachnamen bob studehi zu.
name =  a[1]+a[14]+a[1]+a[-1]+a[-1]+a[-9:-6]+a[3:5]+a[7:9]
print (name)

# Benutze dafür nur die Buchstaben aus der Variable alphabet
# Ändere mithilfe der upper Methode den Anfangsbuchstaben des Vor- und Nachnamens
name = name[0].upper() + name[1:4] + name[4].upper() + name[5:]
print(name)

# Printe den Nachnahmen mit Slicen der name Variable
leer_index = name.find(" ")
nachname = name[leer_index+1:]
print(nachname)

# Erstelle eine Variable name_9999, in der dein Name 9999-mal gespeichert ist

name_9999 = name * 9999
#print(name_9999)





