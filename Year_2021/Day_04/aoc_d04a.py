

def winner(card):
    # First check for a full row:
    for row in card:
        winner = True

        for col in row:
            if not col['marked']:
                winner = False
                break

        if winner:
            return True

    # Now check for a full column
    for col_nr in range(5):
        winner = True

        for row in card:
            if not row[col_nr]['marked']:
                winner = False
                break

        return winner


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

# Read first line
balls_str = lines[0].split(',')
balls = []
for ball_str in balls_str:
    balls.append(int(ball_str))

# delete first line
del lines[0]

# Calculate number of cards:
nr_of_cards = int(len(lines)/6)

# Read the cards
cards = []
current_line = 1
for card_nr in range(nr_of_cards):
    card = []

    for row_nr in range(5):
        row = []
        elements = lines[current_line].split()

        for col_nr in range(5):
            col = {
                'value': int(elements[col_nr]),
                'marked': False,
            }
            row.append(col)

        card.append(row)
        # Advance line
        current_line += 1

    cards.append(card)
    # Ignore empty line
    current_line += 1


# Now play the game
winning_card = -1
for ball in balls:
    for card_nr in range(len(cards)):
        for row in cards[card_nr]:
            for col in row:
                if col['value'] == ball:
                    col['marked'] = True

        if winner(cards[card_nr]):
            winning_card = card_nr
            last_ball = ball
            break

    if winning_card >= 0:
        break

print("last ball is:", last_ball)
print("Winning card:", winning_card)

# Calculate sum
total_unmarked = 0

for row in cards[winning_card]:
    for col in row:
        if not col['marked']:
            total_unmarked += col['value']

print("Total sum:", total_unmarked)
print("Product:", last_ball * total_unmarked)