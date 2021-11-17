# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#  Rodrigo, Dani, Lucas, Flavio

import random

#choice function

#lista = names
#sorteio = random.choice(lista)
#print(sorteio, "is going to buy the meal today!" )

#jeito certo

numero_de_nomes = len(names)
variavel_aleatoria = random.randint(0, numero_de_nomes - 1)
pessoa_que_pagara = names[variavel_aleatoria]
print(pessoa_que_pagara, "is going to buy the meal today!")





