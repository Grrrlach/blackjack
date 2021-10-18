import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Deck():
    def __init__(self):
        self.cards = Deck.cards

    cards = []
    def build(self):
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for v in ["Ace", 2, 3,4,5,6,7,8,9,10, "Jack", "Queen", "King"]:
                self.cards.append([v, suit, v])
                for card in self.cards:
                        if card [-1]== "Ace":
                            card [-1] = 11
                        if card [-1]=="Jack":
                            card[-1]=10
                        if card [-1] == "Queen":
                            card [-1] = 10
                        if card [-1] == "King":
                            card [-1] = 10

class Game_functions():
    used_cards = []
    player_hand = []
    comp_hand = []
    deck = Deck()
    avail_cards = Deck.cards
    random.shuffle(avail_cards)
    new_line = "\n"
    player_total = int()
    comp_total = int()
    
    def __init__(self):
        self.self = self
        self.first_deal()
        

    def first_deal():
        Game_functions.player_hand.append(Game_functions.avail_cards.pop())
        Game_functions.player_hand.append(Game_functions.avail_cards.pop())
        print("Your cards are:")
        for card in Game_functions.player_hand:
            print (f"{card[0]} of {card[1]}")
        Game_functions.comp_hand.append(Game_functions.avail_cards.pop())
        Game_functions.comp_hand.append(Game_functions.avail_cards.pop())
        print (f"{Game_functions.new_line}The Dealer's cards are: ")
        print ("|?|")
        for card in Game_functions.comp_hand:
            if card is not Game_functions.comp_hand[0]:
                print (f"{card[0]} of {card[1]}")

    def player_hit():
        Game_functions.player_hand.append(Game_functions.avail_cards.pop())
        print("Your cards are:")
        for card in Game_functions.player_hand:
            print (f"{card[0]} of {card[1]}")
        print (f"{Game_functions.new_line}The Dealer's cards are: ")
        print ("|?|")
        for card in Game_functions.comp_hand:
            if card is not Game_functions.comp_hand[0]:
                print (f"{card[0]} of {card[1]}")
                
    def is_bust():
        Game_functions.player_total = 0
        Game_functions.comp_total = 0
        for card in Game_functions.player_hand:
            Game_functions.player_total = Game_functions.player_total + card[-1]
        for card in Game_functions.comp_hand:
            Game_functions.comp_total = Game_functions.comp_total + card[-1]
        while Game_functions.player_total > 21:
            Game_functions.player_total = 0
            for card in Game_functions.player_hand:
                if card[0]=="Ace" and card[-1]==11:
                    card[-1] = 1
                    print("ace has been converted") #DELETE
                    Game_functions.player_total = Game_functions.player_total + card[-1]
                else:
                    Game_functions.player_total = Game_functions.player_total + card[-1]
            # print (f"{Game_functions.new_line}Your Hand is: ")
            # for card in Game_functions.player_hand:
            #     print (card[:2])

            break
        # if Game_functions.player_total<=21 and Game_functions.player_total>=Game_functions.comp_total:
        #     print (f"{Game_functions.new_line}Your final hand is:") 
        #     for card in Game_functions.player_hand:
        #         print (card [:2])
        #     print (f"{Game_functions.player_total} points{Game_functions.new_line}")
        #     print (f"{Game_functions.new_line}The Dealer's final hand is:")
        #     for card in Game_functions.comp_hand:
        #         print(card[:2])
        #     print (f"{Game_functions.comp_total} points")
            
        #     print(f"Your total is {Game_functions.player_total}.")
        #     print (f"The Dealer's total is {Game_functions.comp_total}.")


    def comp_hits():
        while True:
            Game_functions.comp_total = 0
            for card in Game_functions.comp_hand:
                Game_functions.comp_total = Game_functions.comp_total + card[-1]
            if Game_functions.comp_total<17:
                Game_functions.comp_hand.append(Game_functions.avail_cards.pop())
                print("The Dealer draws a card.")

            if Game_functions.comp_total>21:
                Game_functions.comp_total = 0
                for card in Game_functions.comp_hand:
                    if card[0]=="Ace" and card[-1]==11:
                        card[-1] = 1
                    Game_functions.comp_total = Game_functions.comp_total + card[-1]
            else:
                print ("The Dealer stays.")
                print(f"{Game_functions.new_line}The Dealer's cards are: ")
                for card in Game_functions.comp_hand:
                    print (f"{card[0]} of {card[1]}")
                break

                
                
    def who_won():
        print(f"{Game_functions.new_line}Your hand is:")
        for card in Game_functions.player_hand:
            print (f"{card[0]} of {card[1]}")
        print(f"{Game_functions.player_total} points{Game_functions.new_line}")
        print("The computer's hand is:")
        for card in Game_functions.comp_hand:
            print(card[:-1])
        print (f"{Game_functions.comp_total} points{Game_functions.new_line}")
        if Game_functions.comp_total >21:
            print ("DEALER BUSTS! Congratulations! You win!")
        elif Game_functions.player_total > 21:
            print (f"Your total is {Game_functions.player_total} points")
            print ("YOU BUSTED! The Dealer wins.")
        elif Game_functions.comp_total <= Game_functions.player_total:
            print ("CONGRATULATIONS! You beat the dealer! YOU WIN!")
        elif Game_functions.comp_total > Game_functions.player_total:
            print ("What's that sound? OH NO! It's the WHAAAAAAA-mbulance coming to pick you up, because YOU LOSE!")
                
                

class UI(): 
    @classmethod
    def play_game(cls):
        while True:
            my_deck = Deck()
            my_deck.build()
            Deck.cards = []
            Game_functions.player_hand = []
            Game_functions.comp_hand = []
            Game_functions.player_total = 0
            Game_functions.comp_total = 0
            start = ''
            start = input ("Would you like to start a new game? Enter 'Y' or 'N': ")
            if start.lower() == 'n':
                clear_screen()
                print (f"{Game_functions.new_line}You chose not to play. {Game_functions.new_line}A strange game...The only winning move is not to play.{Game_functions.new_line}{Game_functions.new_line}Great to meet you, though! {Game_functions.new_line}Maybe it's time to play outside, or read a nice book?")
                break
            elif start.lower() == 'y':
                clear_screen()
                Game_functions.avail_cards = my_deck.cards
                random.shuffle(Game_functions.avail_cards)
                Game_functions.player_total = 0
                Game_functions.player_hand = []
                Game_functions.comp_hand = []
                print (Game_functions.player_hand)
                print (Game_functions.comp_hand)
                Game_functions.first_deal()
                while True:
                    if Game_functions.player_total <= 21:
                        hit = input ("Would you like to 'hit'? Enter 'Y' or 'N': ")
                    elif Game_functions.player_total > 21:
                        hit = 'n'
                        input (f"You may not draw any more cards. Your current total is {Game_functions.player_total}. Press Enter to continue...")
                    if hit.lower() == 'n':
                        clear_screen()
                        Game_functions.comp_hits()
                        Game_functions.is_bust()   
                        input (f"{Game_functions.new_line}Press enter to see who won! ")
                        clear_screen()
                        Game_functions.who_won()
                        break
                    if hit.lower() == 'y':
                        clear_screen()
                        Game_functions.player_hit()
                        Game_functions.is_bust()
                        continue
                    else:
                        print ("That's not a 'Y' or 'N', dummy. Try again!")
            else:
                print('else')
                continue
        play_again = input ("...orrrrrr, maybe you want me to ask you to play a new game?? Enter 'Y' or 'N': ")
        while True:
            if play_again.lower() == 'y':
                Game_functions.player_hand = []
                Game_functions.comp_hand = []
                Game_functions.player_total = 0
                Game_functions.comp_total = 0
                start = ''
                UI.play_game()
            elif play_again.lower() == 'n':
                print (f"{Game_functions.new_line}{Game_functions.new_line}Well, enjoy your book.{Game_functions.new_line}See you next time!{Game_functions.new_line}")
                break
            else:
                continue

        
            
            
        
            
my_game = UI()
my_game.play_game()