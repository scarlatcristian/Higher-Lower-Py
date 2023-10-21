from art import versus
import random

personalities = [
    {"name": "Shakira", "followers": 5,
     "description": "is a Colombian singer and songwriter. Born and raised in Barranquilla, she has been referred to as the 'Queen of Latin Music' and has been praised for her musical versatility."},
    {"name": "Ronaldo", "followers": 4, "description": "is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards"},
    {"name": "Tesla", "followers": 1,
     "description": "was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist best known for his contributions to the design of the modern alternating current (AC) electricity supply system."},
    {"name": "Vid Diesel", "followers": 2,
     "description": "is an American actor and film producer. One of the world's highest-grossing actors, he is best known for playing Dominic Toretto in the Fast & Furious franchise."},
    {"name": "Messi", "followers": 6, "description": "also known as Leo Messi, is an Argentine professional footballer who plays as a forward for and captains both Major League Soccer club Inter Miami and the Argentina national team."},
    {"name": "David Beckham", "followers": 3,
     "description": "is an English former professional footballer, the current president and co-owner of Inter Miami and co-owner of Salford City. Known for his range of passing, crossing ability, and bending free-kicks as a right winger, Beckham has been hailed as one of the greatest and most recognisable midfielders of his generation"}
]


def play_game():
    score = 0
    lives = 1
    right_answer = ""
    pick1 = random.choice(personalities)

    while lives > 0:
        pick2 = random.choice(personalities)

        while pick1 == pick2:
            pick2 = random.choice(personalities)

        followers_pick1 = pick1["followers"]
        followers_pick2 = pick2["followers"]
        name_pick1 = pick1["name"]
        name_pick2 = pick2["name"]
        description_pick1 = pick1["description"]
        description_pick2 = pick2["description"]

        if followers_pick1 > followers_pick2:
            right_answer = 'a'
        else:
            right_answer = 'b'

        print(f"Compare A: {name_pick1} {description_pick1}")
        versus()
        print(f"Against B: {name_pick2} {description_pick2}\n")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == right_answer:
            score += 1
            print(f"Correct, your score is: {score}\n")
            pick1 = pick2
        else:
            lives -= 1

    print(f"Game over, your total score is: {score}")


play_game()
