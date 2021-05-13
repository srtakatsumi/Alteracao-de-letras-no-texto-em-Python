def cripto (frase): """ definimos uma variável que irá armazenar a frase"""
	tradutor = " "  """ variável vazia para depois armazenar o código


   	for letra in frase: """ criamos um laço de for que lerá letra a letra da frase"""


   		if letra in "Aa": """ Se a frase possuir a letra A minuscula ou maiuscula
            		tradutor = tradutor + "1" """ essa letra sera substituida pelo caractere que está entre aspas"""

		elif letra in "Ee":

			tradutor = tradutor + "2"
          	elif letra in "Ii":
           		tradutor = tradutor + "3"
            	elif letra in "Oo":
            		tradutor = tradutor + "4" 
            	elif letra in "Uu":
            		tradutor = tradutor + "5"
            	else:

			tradutor += letra

	return tradutor
print(cripto(input("\n Digite aqui sua frase: \n")))
