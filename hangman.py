from numpy import random

lst = ['marginal']
def game():
    def add_wrd():
        answer = input('Do you wish to add a word to the list? Type Yes or No')
        if answer.title() == 'Yes':
            which_wrd = input('Which word do you want to enter?')
            lst.append(which_wrd.lower())
            add_wrd()
        elif answer.title() == 'No':
            print('Ok, we will pick one from our list. Have fun!')
        else:
            print('Invalid input')
            add_wrd()

    add_wrd()

    wrd = random.choice(lst)
    letters_in_wrd = []
    for i in range(len(wrd)):
        letters_in_wrd.append(wrd[i])

    guesses_left = 6
    score = 0
    running = True
    letters_guessed = []

    while running:
        question = input('There are {} letters in this word. Guess one'.format(str(len(wrd))))
        print('you guessed ' + question)

        if question == '.':
            print('Clever! You know the placeholder value, but I accounted for this!')

        elif question.lower() in letters_in_wrd:
            print(question + ' is in the word')
            score += 1
            print(question + ' was in position ' + str(letters_in_wrd.index(question.lower())+1) + ' of the word')
            letters_in_wrd[letters_in_wrd.index(question.lower())] = '.'
            times_appeared = 0
            try:
                indx = letters_in_wrd.index(question.lower())
            except ValueError:
                indx = -1
            while indx >= 0:
                try:
                    indx = letters_in_wrd.index(question.lower())
                except ValueError:
                    indx = -1
                times_appeared +=1
                if indx != -1:
                    print('it was also in position ' + str(letters_in_wrd.index(question.lower())+1) + ' of the word')
                    letters_in_wrd[letters_in_wrd.index(question.lower())] = '.'
            if times_appeared > 1:
                print(question + ' is in the word ' + str(times_appeared) + ' times')
                score += times_appeared - 1

        elif question.lower() in letters_guessed:
            print('You already guessed ' + question)

        else:
            print(question + ' is not in the word')
            guesses_left += -1
            print('you have ' + str(guesses_left) + ' guesses left')

        letters_guessed.append(question.lower())

        if guesses_left == 0:
            print('Sorry, you have lost')
            running = False
            print('The word was ' + str(wrd))

        if score == len(wrd):
            print('Congrats, you win!!!')
            print('The word was ' + str(wrd))
            running = False



    if running == False:
        response = input('Do you wish to play again? Type Yes or No')
        if response.title() == 'No':
            pass
        elif response.title() == 'Yes':
            game()

game()