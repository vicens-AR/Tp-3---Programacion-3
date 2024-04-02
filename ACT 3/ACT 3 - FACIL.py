registro_edades = {
    'Mati': 30,
    'Martina': 25,
    'Lucas': 40,
    'Negro': 35
}

print("Registro de edades:", registro_edades)

# se agrega al diciionario a Maxi
registro_edades['Maxi'] = 28
print("Registro después de agregar a Maxi:", registro_edades)

# Eliminar una persona del registro
del registro_edades['Negro']
print("Registro después de eliminar al Negro:", registro_edades)

# Buscar la edad de una persona
persona_buscada = 'Martina'
if persona_buscada in registro_edades:
    print("La edad de", persona_buscada, "es", registro_edades[persona_buscada])
else:
    print(persona_buscada, "no se encuentra en el registro de edades.")