from decoration import logo, final_goodbye
from wonders_data import data
import random
import os

# Declare a score variable to keep track of the score
score = 0
# Declare a repeat_game flag which will allow to loop over the same untill it is set to false
repeat_game = True
wonder_b = random.choice(data)

# Initial game statements
print("Welcome to the WonderWorld game!\nDid you know that there are 14 Wonders of the World on our planet?")
print("7 of them belong to the Modern World and the other 7 belong to the Ancient World.")
print("But could you place them in time?? Let's test Your Knowledge!!\n")


# Display logo
# Print game rules
def introduction_game():
    print(logo)
    print("GAME RULES: Two random wonders will be compared with eachother.\nType 'A' or 'B' if you think your choice is the Wonder that was built before the other.\n")
    print("Example : 'Type 'A' for: Chicken Itza, a complex of Mayan ruins on Mexico's Yucatan Peninsula, in Mexico\nOR Type 'B' for: The Christ Redeemer, a large statue of Jesus Christ in Rio de Janeiro, in Brazil")
    print("The correct answer is 'A' as it was built in 800 AC, while 'B' in 1922. HAVE FUN!!\n\n")


def clear_screen():
    """
    Will cls the screen if os == to Windows else clear the screen
    when the function will be called
    """
    os.system('cls' if os.name == 'nt' else 'clear')


introduction_game()


"""
 This loop will repeat the game untill the condition repeat_game will be set to False. This will happen
 when a valid but incorrect answer by the user will be given
 """
while repeat_game:
    
    def build_the_option(wonder):
        """
        Use the wonder data to build the game options and return a readable format.
        """
        wonder_name = wonder["name"]
        wonder_description = wonder["description"]
        wonder_country = wonder["country"]
        return f"{wonder_name}, {wonder_description}, from {wonder_country}"


    def check_user_answer( answer,a_years, b_years):
        """
        Accept user answer and year of wonder 'a' and 'b'
        Call the validate_data function to validate that the answer given is valid
        before checking that the answer given is correct
        Use if-else statement to compare the two options against the user answer:
        - if int wonder_a < int wonder_b (i.e it was built before), and the user choose
        'a' return 'a' as True, if the user choose 'b' and wonder_b < a return 'b' as True else return False
        
        """
        
        validate_data(answer)
        if wonder_a_years < wonder_b_years:
            return answer == 'a'
            
        else:
            return answer == 'b'


    def validate_data(answer):
        """
        Check for the validity of the answer given by the answer
        Accept the user answer and raise and error if the answer given
        is not "a" or "b"
        """
        try:
            if answer !="a" and answer !="b":
                raise ValueError(
                    print(f"Invalid answer. Your answer was: {answer}.\n")
                )
        except ValueError as e:
            print(f"Please type 'a' or 'b'\n")

    
    """
    Using the random module, generate a random wonder
    assign the wonder_a to the wonder_b declared outside the first while loop on line 10,
    so that if the answer is correct, on the next iteration the correct answer will be now the first option
    against a new random wonder option
    """
    wonder_a = wonder_b
    wonder_b = random.choice(data)

    # Prevent the same wonder to be compared
    while wonder_a == wonder_b:
        wonder_b = random.choice(data)


    print(f"Type 'A' for: {build_the_option(wonder_a)}")
    print("OR")
    print(f"Type 'B' for: {build_the_option(wonder_b)}")

    # Ask the user for a guess
    
    answer = input("Which one was built first? 'A' or 'B'?: \n").lower()


    # Retrieve int year_built from wonders_data dictionary to get the year of each wonder
    
    wonder_a_years = wonder_a["year_built"]
    wonder_b_years = wonder_b["year_built"]

    # Call check_user_answer function to establish if the user guess it's right or not
    correct_answer = check_user_answer(answer,wonder_a_years, wonder_b_years)
    """
    -Give user feedback on their guess if the answer is valid
    -Track the score
    -When the game is over add the option to play again and start the game all over
      -If the user wants to play again, clear the screen and start the game again
      -if the user doesn't want to play anymore, quit the game, say 'bye' to the user and print all the description from wonders_data
      to show the user all the wonders from Ancient and Modern world in a readle format
    """
    if answer == 'a' or answer == 'b':
        if correct_answer: 
            score += 1
            print(f"Wonderfull!! That's correct! Current score: {score}\n")
            
        else:
            repeat_game = False
            print(f"You are wrong! End of the game. Final score: {score}")
            new_game = input(f"Want to play again? 'Y' or 'N':\n").lower()
            if new_game == "y":
                clear_screen()
                print("NICE TO SEE YOU AGAIN!!")

                introduction_game()
                repeat_game = True
            elif new_game== 'n':
                clear_screen()
                print(f"{final_goodbye}\n")
                print(f"BUT WAIT!! Before you go, check this out!! Below all the Wonder of the Ancient World and Modern World: \n")
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
                 print(f"Invalid answer: {new_game}. Please type 'y' if you want to keep playing or 'n' if you want to quit the game\n")
                 new_game = input(f"Want to play again? 'Y' or 'N': \n").lower()
                




