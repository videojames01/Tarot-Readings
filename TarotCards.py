import random

# List of cards
golden_dawn = ["The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers",
               "The Chariot", "Justice", "The Hermit", "The Wheel of Fortune", "Strength", "The Hanged Man",
               "Death", "Temperance", "The Devil", "The Blasted Tower", "The Star", "The Moon", "The Sun", "Judgement",
               "The Universe", "The Fool"]
rider_waite_smith = ["The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
                     "The Lovers", "The Chariot", "Justice", "The Hermit", "Wheel of Fortune", "Strength",
                     "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon",
                     "The Sun", "Judgement", "The World", "The Fool"]
book_of_thoth = ["The Magus", "The Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers",
                 "The Chariot", "Adjustment", "The Hermit", "Fortune", "Lust", "The Hanged Man", "Death", "Art",
                 "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "The Aeon", "The Universe", "The Fool"]


# Generate cards
card1 = random.randint(0, 21)
card2 = random.randint(0, 21)
card3 = random.randint(0, 21)

# If there are duplicate cards
if card1 == card2 or card1 == card3:
    card1 = random.randint(0, 21)
if card2 == card1 or card2 == card3:
    card2 = random.randint(0, 21)
if card3 == card1 or card3 == card2:
    card3 = random.randint(0, 21)

# Reversed or upright
up_or_down1 = random.randint(0, 1)
if up_or_down1 == 0:
    direction1 = "upright"
elif up_or_down1 == 1:
    direction1 = "reversed"

up_or_down2 = random.randint(0, 1)
if up_or_down2 == 0:
    direction2 = "upright"
elif up_or_down2 == 1:
    direction2 = "reversed"

up_or_down3 = random.randint(0, 1)
if up_or_down3 == 0:
    direction3 = "upright"
elif up_or_down3 == 1:
    direction3 = "reversed"
