sorok = open('2024.04.22/jelado.py', encoding='utf-8')
lista = []
for sor in sorok:
    for oszlop in sor:
        lista.append(oszlop)
db = 0

while db < len(lista):
    db += 1

print(db)