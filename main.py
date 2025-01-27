from random import randint
from art import logo
print(logo)
intro = "Bem vindo ao jogo Maior ou Menor: Digite 1 se você acha que o primeiro número é maior e 2 se o segundo número é maior: "

score = 0
first_number = randint(1,100)
second_number = randint(1,100)

def greather_lower(f_number, s_number, score):
    end_game = False
    
    type_answer = int(input("Digite 1 para escolher o primeiro, 2 para escolher o segundo! "))

    while not end_game:
        type_answer
        if type_answer == 1 and f_number > s_number:
            print("parabéns você acertou")
            score=+score+1
            print(f"Sua pontuação é: {score}")
            end_game = True

        elif type_answer == 1 and f_number < s_number:
            print("Você perdeu!!")
            print(f"Sua pontuação é: {score}")
            end_game = True

        elif type_answer == 2 and f_number > s_number:
            print("Você perdeu!!")
            print(f"Sua pontuação é: {score}")
            end_game = True

        elif type_answer == 2 and f_number < s_number:
            print("Parabéns você acertou!!")
            score=+score+1
            print(f"Sua pontuação é: {score}")
            end_game = True

        elif type_answer == 1 and f_number == s_number:
            print("Você perdeu!!")
            print(f"Sua pontuação é: {score}")
            end_game = True
            
        elif type_answer == 2 and f_number == s_number:
            print("Você perdeu!!")
            print(f"Sua pontuação é: {score}")
            end_game = True


print(intro)
greather_lower(first_number,second_number, score)
