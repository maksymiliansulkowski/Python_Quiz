import hashlib
import csv
import random
from sys import exit
import datetime
from datetime import timedelta

filename = ''
vocabulary = {}


def main():
    global filename
    filename = input('File name you want to study: ')
    practice = input('Practice (e)english translation, or (f)foreign language? Type \'e\' or \'f\': ')
    if practice == 'e':
        start_eng()
    elif practice == 'f':
        start_foreign()
    else:
        print('Not a valid input, please restart the program.')
        end()


# End the game
def end():
    print('See you later!')
    print('...................')
    exit()


# Start the english translation version
def start_eng():
    # Specify number of rounds
    max_rounds = int(input('Number of rounds to study? Enter number: '))
    print('...................')
    print('Let\'s get started!')
    print('...................')

    # Tables for vocab that were guessed right and wrong
    right = []
    wrong = []

    # Read CSV and add to dictionary
    with open(filename, encoding='utf8') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            vocabulary[row['characters']] = row['english']
        # Take a test with x rounds
        turns = 0
        while turns < max_rounds:
            for _ in vocabulary:
                turns += 1
                print(turns)
                vocab = str(random.choice(list(vocabulary.keys())))
                translation = str(vocabulary[vocab])
                print(vocab)
                guess = input('Translate this: ')
                if guess == translation:
                    print('Correct!')
                    right.append(vocab)
                elif guess != translation:  # User gets one more try
                    guess2 = input('Wrong. Try again: ')
                    if guess2 == translation:
                        print('Correct!')
                        right.append(vocab)
                    else:
                        print('Wrong. Move on.')
                        wrong.append(vocab)
                else:
                    print('Error. Try again.')
                    break
                break
                # Provide summary of test performance
    right_count = len(right)
    wrong_count = len(wrong)
    print('...................')
    print('Test results: ')
    print('Correct: %d' % right_count)  # How many values are correct
    print('Wrong: %d' % wrong_count)  # How many values are wrong
    print('Your score:', (right_count / max_rounds * 100), '%')  # Test score
    print('...................')

    # Print list of words that were wrong, if any
    print('')
    if not wrong:
        data_1 = datetime.datetime.now() + timedelta(days=7)
        data_1str = str(data_1)
        print("Repeat these words until: " + data_1str)
        x = input('Great job! Study again? Type y/n: ')
        print('...................')
        if x == 'y':
            start_eng()
        elif x == 'n':
            end()
    else:
        print('Great job! Study these words again:')
        study_again = list(wrong)
        print(study_again)

        # Saving progress

        textfile = open("progress.txt", "w")
        t = datetime.datetime.now()
        t_string = str(t)
        textfile.write(t_string + "\n")
        textfile.write("")
        for element in study_again:
            textfile.write(element + "\n")
        textfile.close()

        print('...................')
        x = input('Great job! Study again? Type y/n: ')
        print('...................')
        if x == 'y':
            start_eng()
        elif x == 'n':
            end()


# Start the foreign language test
def start_foreign():
    # Specify number of rounds
    max_rounds = int(input('Number of rounds to study? Enter number: '))
    print('...................')
    print('Let\'s start!')
    print('Type \'y\' then ENTER if you get it correct, \'n\' if incorrect.')
    print('...................')

    # Tables for vocab that was right and wrong
    right = []
    wrong = []

    # Read CSV and add to dictionary
    with open(filename, encoding='utf8') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            vocabulary[row['characters']] = row['english']  # zamienione miejscami...

    # Take a test with x rounds
    turns = 0
    while turns < max_rounds:
        for _ in vocabulary:
            turns += 1
            print(turns)
            vocab = str(random.choice(list(vocabulary.keys())))
            translation = str(vocabulary[vocab])
            print(translation)
            guess = input('Translate this: ')
            if guess == vocab:
                print('Correct!')
                right.append(vocab)
            elif guess != vocab:  # User gets one more try
                guess2 = input('Wrong. Try again: ')
                if guess2 == vocab:
                    print('Correct!')
                    right.append(vocab)
                else:
                    print('Wrong. Move on.')
                    wrong.append(vocab)
            else:
                print('Error. Try again.')
                break
            break

        # Provide summary of test performance
    right_count = len(right)
    wrong_count = len(wrong)

    print('...................')
    print('Test results: ')
    print('Correct: %d' % right_count)  # How many values are correct
    print('Wrong: %d' % wrong_count)  # How many values are wrong
    print('Your score:', (right_count / max_rounds * 100), '%')  # Test score
    print('...................')
    # return wrong

    # Print list of words that were wrong, if any
    print('')
    if not wrong:
        data_1 = datetime.datetime.now() + timedelta(days=7)
        data_1str = str(data_1)
        print("Repeat these words until: " + data_1str)
        x = input('Great job! Study again? Type y/n: ')
        print('...................')
        if x == 'y':
            start_foreign()
        elif x == 'n':
            end()
    else:
        print('Great job! Study these words again:')
        study_again = list(wrong)
        print(study_again)

        # Saving progress

        textfile = open("progress.txt", "w")
        t = datetime.datetime.now()
        t_string = str(t)
        for element in study_again:
            textfile.write(element + "\n")
            textfile.write(t_string + "\n")
        textfile.close()

        print('...................')
        x = input('Great job! Study again? Type y/n: ')
        print('...................')
        if x == 'y':
            start_eng()
        elif x == 'n':
            end()


def signup():
    usr = input('Enter username: ')
    pwd = input('Enter password : ')
    conf_pwd = input('Confirm password: ')
    i = id(usr)
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open('users.txt', 'w') as f:
            f.write(usr + '\n')
            f.write(hash1 + '\n')
            f.write(str(i))
        f.close()
        print('You have registered successfully!')
        login()
    else:
        print('Password is not same as above! \n')


def login():
    print('Login')
    usr = input('Enter username: ')
    pwd = input('Enter password: ')
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('users.txt', 'r') as f:
        stored_usr, stored_pwd, stored_id = f.read().split('\n')
    f.close()
    if usr == stored_usr and auth_hash == stored_pwd:
        print('Logged in Successfully! \n')

        # Loading progress

        f = open('progress.txt', 'r')
        file_contents = f.read()
        print('Repeat these words: ')
        print(file_contents)
        f.close()
        main()
    else:
        print('Login failed! \n')


while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
