name = "Donald Trump"

# String in vor- nachname teilen
name_teilen = name.split(" ")
vorname = name_teilen[0]
nachname = name_teilen[1]

neuer_vorname = nachname[0]+ vorname[1:]
neuer_nachname = vorname[0] + nachname[1:]

neuer_name = neuer_vorname + " " + neuer_nachname
print(neuer_name)