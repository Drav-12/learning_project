# LISTAS
notas = [8, 12, 15, 16, 17]

promedio = sum(notas) / len(notas)

print(len(notas))
print(f"La nota es {promedio}")

if promedio > 10:
    print("APROBADO")
else:
    print("DESAPROBADO")


# ITERATIVAS
# 1. CONDICION
print("###########################################")
print("INICIO DEL PROGRAMA")

ahorro = 200

while ahorro < 1200: # MIENTRAS
    ahorro = ahorro + 35
    print(f"DIA {(ahorro//35)}: El ahorro actual es: {ahorro}")
print(f"El ahorro final fue {ahorro}")


# 2. LISTAS
nombres = ["Diana", "Celeste", "Ariana", "Claudia", "Estefania"]
for nombre in nombres: # PARA/EN
    print(f"Hola {nombre}, espero que estes bien, estuve pensando ti, eres la unica.")


# 3. TRY-EXCEPT
print("###########################################")
try:
    print(120/2)
except:  # noqa: E722
    print("NO SE PUDO PIPIPI")