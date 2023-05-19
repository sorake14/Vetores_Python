#Soma de Vetores:

vetor1 = [10, 9.5, 9, 10]
vetor2 = [7, 3, 2, 8]

def calcular_media(notas):
    soma = sum(notas)
    media = soma/ len(notas)
    return media

media_vetores1 = calcular_media(vetor1)
media_vetores2 = calcular_media(vetor2)

media_final = (media_vetores1 + media_vetores2) / 2

print (media_final)
