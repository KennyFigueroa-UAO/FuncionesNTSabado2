# Como puedo crear 200 notas de 1 a 5 en python
# Sin pedir los datos al usuario
# sin quemar los datos manualmente
import random

notas = []

for i in range(5):
    nota = random.randint(1,10)
    notas.append(nota)

#tupla que es y valores aleatorios decimales
print(notas)
notas.insert(0,80)
print(notas)
notas.insert(1,90)
notas.insert(1,90)
print(notas)
notas.remove(90)
print(notas)
notas.pop(0)
print(notas)
notas.sort()
print(notas)
notas.clear()
print(notas)