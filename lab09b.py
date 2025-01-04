import cards_B as cards #import the cards_B.py module so that you can use it in your code




# Create the deck of cards
the_deck = cards.Deck()
the_deck.shuffle()

"\n:~Keep Going: (Nn) to stop ~:"
"Starting Hands"
"Hand1:"
"Hand2:"
"hand1:"
"hand2:"
"Player 1 wins!!!"
"Player 2 wins!!!"
"Battle was 1: {}, 2: {}. Player 1 wins battle."
"Battle was 1: {}, 2: {}. Player 2 wins battle."
"Battle was 1: {}, 2: {}. Battle was a draw."

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( the_deck.deal() )
    player2_list.append( the_deck.deal() )

print("Starting Hands")
print('Hand1:', player1_list)
print('Hand2:', player2_list)
print('')

stop_war = ''
while stop_war.lower() != 'n':

    p1_card = player1_list[0]
    player1_list.remove(p1_card)

    p2_card = player2_list[0]
    player2_list.remove(p2_card)

    if p1_card.rank() > p2_card.rank():
        print(f"Battle was 1: {p1_card}, 2: {p2_card}. Player 1 wins battle.")
        player1_list.append(p1_card)
        player1_list.append(p2_card)
        print('hand1:', player1_list)
        print('hand2:', player2_list)

    elif p1_card.rank() < p2_card.rank():
        print(f"Battle was 1: {p1_card}, 2: {p2_card}. Player 2 wins battle.")
        player2_list.append(p2_card)
        player2_list.append(p1_card)
        print('hand1:', player1_list)
        print('hand2:', player2_list)

    else:
        print(f"Battle was 1: {p1_card}, 2: {p2_card}. Battle was a draw.")
        player1_list.append(p1_card)
        player2_list.append(p2_card)
        print('hand1:', player1_list)
        print('hand2:', player2_list)

    if len(player1_list) == 0:
        print("Player 2 wins!!!")
        break
    elif len(player2_list) == 0:
        print("Player 1 wins!!!")
        break

    stop_war = input("\n:~Keep Going: (Nn) to stop~:")
    if stop_war == "n":
        if len(player1_list) > len(player2_list):
            print("Player 1 wins!!!")
        else:
            print("Player 2 wins!!!")

