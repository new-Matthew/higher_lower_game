import random
from art import logo, versus as vs
from data import data_higher_lower

print(logo)
intro = "Bem vindo ao jogo Maior ou Menor: Digite 1 se você acha que o primeiro número é maior e 2 se o segundo número é maior: "
print(intro)
topic_1 = random.choice(data_higher_lower)
topic_2 = random.choice(data_higher_lower)
if topic_1 == topic_2:
    topic_2 = random.choice(data_higher_lower)

def check_answer(guess_user, topic_value_1, topic_value_2):
    if topic_value_1 > topic_value_2:
        return guess_user == 1
    else:
        return guess_user == 2

def show_before(topic):

    topic_name = topic["name"]
    return f"{topic_name} "


print("Compare: ")
print(f"opção 1: {show_before(topic_1)}. ")
print(vs)
print(f"opção 2: {show_before(topic_2)}. ")

guess = int(input("Digite 1 ou 2: "))

topic_value_1 = topic_1["value"]
topic_value_2 = topic_2["value"]

is_correct = check_answer(guess, topic_value_1, topic_value_2)


