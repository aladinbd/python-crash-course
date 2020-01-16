age_0 = 22
age_1 = 18
print(age_0 == 22)
print(age_1 == 18)

# Test using lower()
motorcycle = 'Honda'
print(motorcycle.lower() == 'honda')

# Numerical Test using and, or keyword
print(age_0 >= 23 or age_1 >= 18)
print(age_0 >= 22 and age_1 >= 18)

# Test whether an item in a list
players = ['aladin', 'alpona', 'arika']
player = 'tulika'
if player not in players:
    print(f"{player.title()}, you're not in the main list.")
