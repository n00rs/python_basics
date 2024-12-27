import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dict_dice = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│       ● │",
       "│    ●    │",
       "│ ●       │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),
}

print(dict_dice)

int_total = 0
list_dice = []
int_num_of_dice = int(input("How many Dice ?:"))

for int_dice in range(int_num_of_dice):
    list_dice.append(random.randint(1,6))

# for print dice vertically
for int_dice in range(int_num_of_dice):
    for line in dict_dice.get(list_dice[int_dice]):
        print(line)
        
# calculating total
for die in list_dice:
    int_total += die
print(list_dice)

# print horizontally
for line in range(5):
    for int_dice in list_dice:
        print(dict_dice.get(int_dice)[line],end="")
    print()
        
print(f" Total :{int_total}")