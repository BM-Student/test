import random

def game_loop(money=25):
    def lost():
        ans = input('You lost, Play again?')
        if ans.lower() == 'yes':
            game_loop()
        elif ans.lower() == 'no':
            print('Bye')
        else:
            print('Invalid input')
            lost()
    coins = money
    if coins > 1:
        print('You have ' + str(coins) + ' coins')
    elif coins == 1:
        print('You have ' + str(coins) + ' coin')
    elif coins <= 0:
        lost()
    bet = 0
    # creating the deck
    suits = ['hearts', 'spades', 'clubs', 'diamonds']
    card_numbers = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    card_values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    zip_cards = list(zip(card_numbers, card_values))
    deck = {}
    for i in suits:
        for j in zip_cards:
            card_key = j[0] + ' of ' + i
            card_value = j[1]
            deck[card_key] = card_value

    def ask_bet():
        init_bet = float(input('How much do you wish to bet?'))
        if type(init_bet) is int or type(init_bet) is float:
            if init_bet > coins:
                print('You don\' have that many coins to bet. Pick a different value')
                ask_bet()
                return 0
            elif init_bet > 0:
                return init_bet
            else:
                print('Invalid input')
                ask_bet()
                return 0
        else:
            print('Invalid input')
            ask_bet()
            return 0

    bet += ask_bet()
    # deal player hand
    player_hand = {}

    for i in range(2):
        card = random.choice(list(deck.items()))
        deck.pop(card[0])
        player_hand[card[0]] = card[1]

    print('Your current hand is ' + str(list(player_hand.keys())))

    def sum_player_hand():
        player_total = 0
        for i in player_hand.keys():
            if i[0:3] == 'ace':
                if player_total + 11 > 21:
                    player_total += player_hand[i][0]
                else:
                    player_total += player_hand[i][1]
            else:
                player_total += player_hand[i]

        print('Your hand adds up to ' + str(player_total))

        if player_total > 21:
            print('You lost this hand')
            return False
        elif player_total == 21:
            return player_total
        else:
            return player_total
    sum_player_hand()

    # deal dealer hand
    dealer_hand = {}

    for i in range(2):
        card = random.choice(list(deck.items()))
        deck.pop(card[0])
        dealer_hand[card[0]] = card[1]

    print('The dealer\'s face up card is ' + random.choice(list(dealer_hand.keys())))

    dealer_total = 0
    for i in dealer_hand.keys():
        if i[0:3] == 'ace':
            if dealer_total + 11 > 21:
                dealer_total += dealer_hand[i][0]
            else:
                dealer_total += dealer_hand[i][1]
        else:
            dealer_total += dealer_hand[i]

    # the function for the dealer's moves
    def dealer_hand_count(wealth, change, hand=dealer_hand):
        def sum_hand():
            hand_total = 0
            for i in hand.keys():
                if i[0:3] == 'ace':
                    if hand_total + 11 > 21:
                        hand_total += hand[i][0]
                    else:
                        hand_total += hand[i][1]
                else:
                    hand_total += hand[i]
            return hand_total
        if sum_hand() < 17:
            card = random.choice(list(deck.items()))
            deck.pop(card[0])
            dealer_hand[card[0]] = card[1]
            dealer_hand_count(coins, bet, dealer_hand)
        elif sum_hand() == 21 or (sum_hand() >= sum_player_hand() and sum_hand() < 21):
            print('The dealer\' hand is ' + str(list(hand.keys())))
            print('The dealer wins')
            wealth += -change
            game_loop(wealth)
        elif sum_hand() > 21:
            print('The dealer\' hand is ' + str(list(hand.keys())))
            print('You won this hand!!')
            wealth += change
            game_loop(wealth)
        elif sum_hand() < sum_player_hand():
            print('The dealer\' hand is ' + str(list(hand.keys())))
            print('You won this hand!!')
            wealth += change
            game_loop(wealth)

    # player moves
    def choice(wealth, change=0):
        if sum_player_hand() == 21:
            print('You won this hand!!')
            wealth += change
            game_loop(wealth)
        answr = input('Do you hit or hold?')
        if answr == 'hit':
            card = random.choice(list(deck.items()))
            deck.pop(card[0])
            player_hand[card[0]] = card[1]
            print('Your drew a ' + str(card[0]))
            if sum_player_hand() is False:
                wealth += -change
                game_loop(wealth)
            elif sum_player_hand() == 21:
                print('You won this hand!!')
                wealth += change
                game_loop(wealth)
            else:
                choice(coins, bet)
        elif answr == 'hold':
            dealer_hand_count(coins, bet, dealer_hand)
    choice(coins, bet)

game_loop()