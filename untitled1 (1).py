# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1159VYf7PKAw1sFRl6GVR0QOkIVJO2wZw
"""

age = int(input("digite sua idade"))
experiencia = input("digite sua experiencia com informatica")
#identação === organização do código em python
if age >= 18 or age <= 65:
    print("você pode votar")
else:
    print("você não pode votar")




if experiencia == "excel" or experiencia == "office":
    print("selecionado(a)")
else:
    print("não pode ser selecionado")


age = 18

if age != 18:
    print("é diferente ")
else:
  print("não é diferente")

if(age == 20) :
    print("maior de idade")

#anotação NOT AND OU
# 1:Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

texto  = "diferente"
texto2 = input("escreva algo")
print(texto + texto2)

#2:Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss"
hora = input("digite o valor entre 0 e 23")
minuto = input("digite um valor entre 0 e 59")
segundos = input("digite um valor entre 0 e 59")

print(hora+":"+ minuto+ ":"+ segundos)

#3:Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.

numero = 11
numero2 = 940028922

print(numero , numero2)

#4:Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.

ingrediente = "pão"
ingrediente2 = "alface"
ingrediente3 = "maionese"
ingrediente4 = "frango"


print(ingrediente +"," ,ingrediente2 +"," ,ingrediente3 +"," ,ingrediente4)



#5:**Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.**

nome = input("digite seu nome")
altura = input("digite sua altura")
peso = input("peso")

print("Diga alguns dos seus dados:", nome ,"," altura , peso)