# projektname = input("Wie heißt du?")
# zusatz = " - digital"
# print(projektname+zusatz)


k = int(input("Wie viele Tassen Kaffee hattest du?"))
if 3 <= k <=8:
    print("ich hatte", k, "Kaffee. Das passt.")  # = print(f"ich hatte {k} Kaffee.")
elif k <= 2:
    print("Ich hatte noch nicht genug KAffee.")
else:
    print("Das war zu viel! Lass mal nicht.")

n = 1
while n < 8:
    print(f"Kaffekonsum {n} ist akzeptabel")
    n = n + 1

else:
    print("Das war zu viel.")

# während Anzahl Kaffee kleiner 8 ist soll string wie oen ausgeführt werden; ansonsten "zu viel Kaffee"


# alles mit Python auf git hochladen
# github installieren und einführung anschauen
