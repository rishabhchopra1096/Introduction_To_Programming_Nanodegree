# Lets start with the basic variables that will remain
# unchanged thoughout the program:

sentence0='\nThe current paraghraph reads as such:'
sentence1="\n\nA common first thing to do in a language is display Hello __1__!'"
sentence2="\nIn __2__ this is particularly easy; all you have to do is type in: "
sentence3='''\n__3__ "Hello __1__!"'''
sentence4="\n\nOf course, that isn't a very useful thing to do. However, it is an "
sentence5="\nexample of how to output to the user using the __3__ command, and "
sentence6="\nproduces a program which does something, so it is useful in that capacity. "
sentence7="\n\nIt may seem a bit odd to do something in a Turing complete language that "
sentence8="\ncan be done even more easily with an __4__ file in a browser, but it's "
sentence9="\na step in learning __2__ syntax, and that's really its purpose. "

# Main quiz question used in all 3 levels:
quiz_question = sentence0 + sentence1 + sentence2+sentence3+sentence4+sentence5
quiz_question += sentence6 +sentence7+sentence8+sentence9

answers = [' ','world','Python','print','HTML']
# answers[0] is set to a blank string to match with the blank_number / number of blanks.

number_of_blanks = 4

levels = ['easy','medium','hard']

# Function 1 :
introduction = "\nPlease select a game difficulty by typing it in! "
introduction += "\nPossible choices include easy, medium, and hard. "
introduction += "\nIf you choose easy, you can select the number of guesses you get per problem."
introduction += "\nEnter 'quit' to quit game. "

def select_level():
    '''Determines level selected by user.
    User can 'quit' the program at this point.'''
    level = raw_input(introduction)
    return level

# function 2:
# This function will be used after the select_level function.
def number_of_trys(level):
    '''Takes in the difficulty level and returns the number
    of trys user will get per blank.'''
    if level == 'easy':
        print("\nSince you've chosen easy, "+
            "\nYou get to choose how many trys you get for every problem!")
        trys=raw_input("Enter the number of guesses you would like per problem. ")
        trys=int(trys)
        return trys
    elif level == 'medium':
        trys = 3
        return trys
    elif level == 'hard':
        trys = 1
        return trys

# function 3 :
def initialising_game(level,quiz_question=quiz_question):
    '''Takes in a level.
    Using number_of_trys function , gets number of trys.
    Prints out the number of trys user will get.
    Sets blank_number and turn_number to 1.
    Also prints out the question paragraph only for the first time.'''
    trys = number_of_trys(level)
    if level == 'easy':
        print('\nOk then, you will get '+str(trys)+' guesses per problem'+
            "\n" + quiz_question)
    elif level == 'medium':
        print("\nYou've chosen medium!"+
        "\n\nYou will get "+ str(trys) + " guesses per problem." +
        "\n" + quiz_question)
    elif level == 'hard':
        print("\nYou've chosen hard!"+
        "\n\nYou will get " + str(trys) + " guess per problem." +
        "\n" + quiz_question)

# function 3:
def won_lost(turn_number,trys):
    '''Determines weather a player won or lost.
    Print out the response accordingly.'''
    if turn_number > trys:
        print('\nGame Over. You exhausted your turns.')
    else:
        print("\n\nCongrats, you won!")
        # Print out the final paragraph with all answers.

# function 4 :
answers = [' ','world','Python','print','HTML']
def play_game(difficulty_level , quiz_question=quiz_question , answers=answers):
    '''Takes in the difficulty level , quiz_questions and their answers.'''
    trys = number_of_trys(difficulty_level) # If level == easy
    initialising_game(difficulty_level)
    blank_number = 1
    turn_number = 1
    while turn_number <= trys and blank_number <= number_of_blanks:
        answer=raw_input("\nWhat should be "+"__"+str(blank_number)+"__"+" be substituted for? ")
        # Asking the user for the answer to respective blank_number
        if answer == answers[blank_number] or answer == answers[blank_number].lower():
        # Checks for lower case also.
            print("\nCorrect!")
            quiz_question = quiz_question.replace("__"+str(blank_number)+"__",answers[blank_number])
            # Replacing all occurences of that blank with its answers
            blank_number += 1 # Changing Question Number
            turn_number = 1 # Re-setting turn_number for next blank / question_number
            print(quiz_question)
            # Shows All occurences of the blank replaced with the answer.
        else: # If the answer is wrong.
            print('\nYou have '+str(trys - turn_number) + ' trys left!')
            # Telling the user how many turns he/she is left with.
            turn_number += 1 # Increasing turn_number as to respect number of trys allowed.
    # Now , once the loop quits : Function will determine weather player won or lost.
    won_lost(turn_number,trys)

# Main Function
def main():
    '''Calls the whole game.'''
    while True:
        difficulty_level = select_level()
        # Setting difficulty level chosen by the user.
        if difficulty_level == 'quit': # Player does not want to play.
            break
        elif difficulty_level in levels:
            play_game(difficulty_level)
        else: # If player enter something other than name of level or quit value.
            print("That's not an option.")

main()





