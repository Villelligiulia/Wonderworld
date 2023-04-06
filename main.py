from decoration import logo
from wonders_data import data
import random


# Display logo
print(logo)
score = 0
repeat_game = True

print("Welcome to the WonderWorld game!\nDid you know that there are 14 Wonders of the World on our planet?")
print("7 of them belong to the Modern World and the other 7 belong to the Ancient World")
print("But could you place them in time?? Let's test Your Knowledge!!\n")
print("GAME RULES: Two random wonders will be compared with eachother\nType 'A' or 'B' if you think your choice is the Wonder that was built before the other.")
print("Example : 'Type 'A' for: Chicken Itza, a complex of Mayan ruins on Mexico's Yucatan Peninsula, in Mexico\nOR Type 'B' for: The Christ Redeemer, a large statue of Jesus Christ in Rio de Janeiro, Brazil, in Brazil")
print("The correct answer is 'A' as it was built in 800 AC, while 'B' in 1922. HAVE FUN!!\n\n")



introduction_game()

while repeat_game:
    
    def build_the_option(wonder):
        """
        Use the wonder data to build the game option and return a readable format.
        """
        wonder_name = wonder["name"]
        wonder_description = wonder["description"]
        wonder_country = wonder["country"]
        return f"{wonder_name}, {wonder_description}, from {wonder_country}"


    def check_user_answer( answer,a_years, b_years):
        """
        Accept user answer and year of wonder 'a' and 'b'
        Call the validate_data function before checking id the answer inserted is valid
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

    
    # Using the random module, generate a random wonder
    wonder_a = random.choice(data)
    wonder_b = random.choice(data)

    # Prevent the same wonder to be compared
    if wonder_a == wonder_b:
        wonder_b = random.choice(data)


    print(f"Type 'A' for: {build_the_option(wonder_a)}")
    print("OR")
    print(f"Type 'B' for: {build_the_option(wonder_b)}")

    # Ask the user for a guess
    
    answer = input("Which one was built first? 'A' or 'B'?: ").lower()


    # Retrieve int year_built from wonders_data dictionary to get the year of each wonder
    # Call check_user_answer function to establish if the user guess it's right or not
    wonder_a_years = wonder_a["year_built"]
    wonder_b_years = wonder_b["year_built"]
    
    
    correct_answer = check_user_answer(answer,wonder_a_years, wonder_b_years)

    # Give user feedback on their guess if the answer is valid
    ## Track the score
    if answer == 'a' or answer == 'b':
        if correct_answer: 
            score += 1
            print(f"Wonderfull!! That's correct! Current score: {score}")
            
        else:
            repeat_game = False
            print(f"You are wrong! End of the game. Final score: {score}")