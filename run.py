from decoration import logo, final_goodbye
from wonders_data import data
import random
import os

score = 0
repeat_game = True
wonder_b = random.choice(data)

print("Welcome to the WonderWorld game!\n")
print("Did you know that there are 14 Wonders of the World on our planet?")
print("7 of them belong to the Modern World,")
print("and the other 7 belong to the Ancient World.")
print("But could you place them in time?? Let's test Your Knowledge!!\n")


def introduction_game():
    print(logo)
    print("GAME RULES: Two random wonders will be compared with eachother.\n")
    print("Type 'A' or 'B' if you think your choice is the Wonder")
    print("that was built first.\n")
    print("Example : 'Type 'A' for: Chicken Itza, a complex of Mayan ruins,")
    print("in Mexico\n")
    print("OR Type 'B' for: The Christ Redeemer, a large statue of")
    print("Jesus Christ,in Brazil")
    print("The correct answer is 'A' as it was built in 800 AC, while 'B'")
    print("in 1922. HAVE FUN!!\n\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


introduction_game()

while repeat_game:
    def build_the_option(wonder):
        wonder_name = wonder["name"]
        wonder_description = wonder["description"]
        wonder_country = wonder["country"]
        return f"{wonder_name}, {wonder_description}, from {wonder_country}"

    def check_user_answer(answer, a_years, b_years):
        validate_data(answer)
        if wonder_a_years < wonder_b_years:
            return answer == 'a'
        else:
            return answer == 'b'

    def validate_data(answer):
        try:
            if answer != "a" and answer != "b":
                raise ValueError(
                    print(f"Invalid answer. Your answer was: {answer}.\n")
                )
        except ValueError as e:
            print(f"Please type 'a' or 'b'\n")

    wonder_a = wonder_b
    wonder_b = random.choice(data)
    while wonder_a == wonder_b:
        wonder_b = random.choice(data)
    print(f"Type 'A' for: {build_the_option(wonder_a)}")
    print("OR")
    print(f"Type 'B' for: {build_the_option(wonder_b)}")

    answer = input("Which one was built first? 'A' or 'B'?: \n").lower()
    wonder_a_years = wonder_a["year_built"]
    wonder_b_years = wonder_b["year_built"]
    correct_answer = check_user_answer(answer, wonder_a_years, wonder_b_years)
    if answer == 'a' or answer == 'b':
        if correct_answer:
            score += 1
            print(f"Wonderfull!! That's correct! Current score: {score}\n")
        else:
            repeat_game = False
            print(f"You are wrong! End of the game. Final score: {score}")
            new_game = input(f"Want to play again? 'Y' or 'N': \n").lower()
            if new_game == "y":
                clear_screen()
                print("NICE TO SEE YOU AGAIN!!")
                introduction_game()
                repeat_game = True
            elif new_game == 'n':
                clear_screen()
                print(f"{final_goodbye}\n")
                print(f"BUT WAIT!! Before you go, check this out!!")
                print(" Below all the Wonder of the two Worlds: \n")
                for my_dict in data:
                    output = ""
                    output += my_dict['name'] + ", "
                    output += my_dict['description'] + ", "
                    output += my_dict['country'] + ", "
                    if my_dict['year_built'] < 0:
                        output += f"{str(abs(my_dict['year_built']))} B.C.\n"
                    else:
                        output += f"{str(my_dict['year_built'])} A.C.\n"
                    print(output)
            else:
                print(f"Invalid answer: {new_game}.Please type 'y' if you want")
                print("to play again 'n' if you want to quit the game\n")
                new_game = input(f"Want to play again? 'Y' or 'N': \n").lower()