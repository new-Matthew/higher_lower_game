import random
from art import logo, versus as vs
from data import data_higher_lower

print(logo)
intro = "Bem vindo ao jogo Maior ou Menor: Digite 1 se você acha que o primeiro número é maior e 2 se o segundo número é maior: "
print(intro)
score = 0
topic_1 = random.choice(data_higher_lower)
topic_2 = random.choice(data_higher_lower)
if topic_1 == topic_2:
    topic_2 = random.choice(data_higher_lower)

def check_answer(guess_user, topic_value_1, topic_value_2):
    topic_value_1 = topic_1["value"]
    topic_value_2 = topic_2["value"]
    if guess_user == 1:
        topic_value_1 = topic_1["value"]

def show_berore(topic):

    topic_name = topic["name"]
    #topic = data_higher_lower["value"]
    #topic = data_higher_lower["answer"]
    return f"{topic_name} "

def show_result(topic):
    
    topic_name = topic["name"]
    #topic_value = topic["value"]
    topic_answer = topic["answer"]
    return f"{topic_name} possui: {topic_answer}"

print("Compare: ")
print(f"opção 1: {show_berore(topic_1)}. ")
print(vs)
print(f"opção 2: {show_berore(topic_2)}. ")

guess = int(input("Digite 1 ou 2: "))

topic_value_1 = topic_1["value"]
topic_value_2 = topic_2["value"]

check_answer(guess, topic_value_1, topic_value_2)

print("Resposta: ")
print(f"opção 1: {show_result(topic_1)}. ")
print(vs)
print(f"opção 2: {show_result(topic_2)}. ")


"""
def greather_lower(f_number, s_number, score):
    end_game = False
    type_answer = int(input("Digite 1 se você acha que o primeiro é maior ou 2 se acha que o segundo é maior! "))
    if type_answer == 1:
        topic_1
    elif type_answer == 2:
        topic_2

    while not end_game:
        type_answer
"""


#greather_lower(topic_1, topic_2, score)
