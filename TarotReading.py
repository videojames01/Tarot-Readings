import TarotCards as tc
import time
import webbrowser

# Choosing a deck
deck_choice = "None"
confirm = "No"
while confirm != "Yes":

    deck_choice = input("Which deck would you like to use? ")

    if deck_choice == tc.decks[0]:
        print("You have chosen the Golden Dawn deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    elif deck_choice == tc.decks[1]:
        print("You have chosen the Rider-Waite-Smith deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    elif deck_choice == tc.decks[2]:
        print("You have chosen the Book of Thoth deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    else:
        print("Please input a valid deck name.")
        confirm = "No"

if deck_choice == "Golden Dawn":
    print("Please wait while your three cards are generated...")
    time.sleep(3)
    print("Your first card is", tc.direction1, tc.golden_dawn[tc.card1])
    time.sleep(2)
    print("Your second card is", tc.direction2, tc.golden_dawn[tc.card2])
    time.sleep(2)
    print("Your third card is", tc.direction3, tc.golden_dawn[tc.card3])
    time.sleep(3)

elif deck_choice == "Rider-Waite-Smith":
    print("Please wait while your three cards are generated...")
    time.sleep(3)
    print("Your first card is", tc.direction1, tc.rider_waite_smith[tc.card1])
    time.sleep(2)
    print("Your second card is", tc.direction2, tc.rider_waite_smith[tc.card2])
    time.sleep(2)
    print("Your third card is", tc.direction3, tc.rider_waite_smith[tc.card3])
    time.sleep(3)

elif deck_choice == "Book of Thoth":
    print("Please wait while your three cards are generated...")
    time.sleep(3)
    print("Your first card is", tc.direction1, tc.book_of_thoth[tc.card1])
    time.sleep(2)
    print("Your second card is", tc.direction2, tc.book_of_thoth[tc.card2])
    time.sleep(2)
    print("Your third card is", tc.direction3, tc.book_of_thoth[tc.card3])
    time.sleep(3)

# View interpretations online
website = input("Would you like to know the meanings of your cards? ")
if website != "Yes":
    print("If you would like to know more, please visit www.biddytarot.com")
    time.sleep(5)
else:
    webbrowser.open("www.biddytarot.com/tarot-card-meanings/major-arcana", new=2)
