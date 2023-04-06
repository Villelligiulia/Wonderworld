from decoration import logo
from wonders_data import data
import random


def build_the_option(wonder):
    """
    Use the wonder data to build the game option and return a readable format.
    """
    wonder_name = wonder["name"]
    wonder_description = wonder["description"]
    wonder_country = wonder["country"]
    return f"{wonder_name}, {wonder_description}, from {wonder_country}"


def check_user_answer(answer, a_years, b_years):
    """
    Accept user answer and year of wonder 'a' and 'b'
    Use if-else statement to compare the two options against the user answer:
    - if int wonder_a < int wonder_b (i.e it was built before), and the user choose
    'a' return 'a' as True, if the user choose 'b' and wonder_b < a return 'b' as True else return False
    """
    if wonder_a_years < wonder_b_years:
        return answer == 'a'
        
    else:
        return answer == 'b'
        


# Display logo
print(logo)

# print("Welcome to the WonderWorld game!\nDid you know that there are 14 Wonders of the World on our planet?")
# print("7 of them belong to the Modern World and the other 7 belong to the Ancient World")
# print("But could you place them in time?? Let's test Your Knowledge!!")
# print("GAME RULES: Two random wonders will be compared with eachother\nType 'A' or 'B' if you think your choice is the Wonder that was built before the other.")
# print("Example : 'Type 'A' for: Chicken Itza, a complex of Mayan ruins on Mexico's Yucatan Peninsula, in Mexico")
# print("Type 'B' for: The Christ Redeemer, a large statue of Jesus Christ in Rio de Janeiro, Brazil, in Brazil")
# print("The correct answer is 'A' as it was built in 800 AC, while 'B' in 1922. HAVE FUN!!")

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
user_guess= input("Which one was built first? 'A' or 'B'?: ").lower()

# Retrieve int year_built from wonders_data dictionary to get the year of each wonder
# Call check_user_answer function to establish if the user guess it's right or not
wonder_a_years = wonder_a["year_built"]
wonder_b_years = wonder_b["year_built"]
correct_answer = check_user_answer(user_guess, wonder_a_years, wonder_b_years)