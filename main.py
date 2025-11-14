import string
import time 


print("---------------------------")
print("  BENVENUTO NEL CIFRARIO  ")
print("---------------------------")

caratteri = string.ascii_lowercase
time.sleep(1)
print("so che hai un codice da cifrare... scrivimelo ")
codice = input("\n")
print("che chiave vuoi usare per cifrarlo? ")
chiave = input("\n")
chiave = int(chiave)
messaggio_criptato =""
for char in codice:
    if char not in caratteri:
        messaggio_criptato = messaggio_criptato + char 
    else:
        indice = caratteri.index(char)
        n_indice = (indice + chiave) % 26
        messaggio_criptato = messaggio_criptato + caratteri[n_indice]

print(messaggio_criptato)


