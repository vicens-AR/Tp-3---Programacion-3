inscripcion = ["h","o","l","a","l","o","c","o",]

frecuencia_inscripcion = {}

for inscri in inscripcion:
    if inscri in frecuencia_inscripcion:
        frecuencia_inscripcion[inscri] +=1
    else:
         frecuencia_inscripcion[inscri] =1

print("la frecuencia de las letras es:", frecuencia_inscripcion)