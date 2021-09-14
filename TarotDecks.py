# List of decks
decks = ["Golden Dawn", "Rider-Waite-Smith", "Book of Thoth"]

# Choosing a deck
confirm = "No"
while confirm != "Yes":

    deck_choice = input("Which deck would you like to use? ")

    if deck_choice == decks[0]:
        print("You have chosen the Golden Dawn deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    elif deck_choice == decks[1]:
        print("You have chosen the Rider-Waite-Smith deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    elif deck_choice == decks[2]:
        print("You have chosen the Book of Thoth deck.")
        confirm = input("Are you sure that this is the deck you want to use? ")
    else:
        print("Please input a valid deck name.")
        confirm = "No"
