#declare the constant variable that don't change their values"

#define the trader = []
TRADER = [
    {'name': 'Sword', 'price': 100, 'stock': 10}, {'name': 'Shield', 'price': 150, 'stock': 5}, {'name': 'Health Potion', 'price': 50, 'stock': 20}, {'name': 'Mana Potion', 'price': 50, 'stock': 20}, {'name': 'Armor', 'price': 200, 'stock': 3}]
#1 while characters < 2
Players = []
while len(Players) < 2:
#1.1 declare charcter profile dicti
#1.2 Ask user to input the following information about their character   
#(Name,Description,Sex,Race)   
#1.3 Confirm Data with user    continue
#1.4 Implement stats generation system  
#('Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma')
#1.5 Implement secondary character stats
#('Health Points','Mana Points','Armor','gold)  
#Allow the user to modify certain stats
#1.6 Confirm the character stats  
 # Recalculate secondary stats
#1.7 Displasy character stats document
#1.8 Ask the player to buy some gear from the trader
#1.9 loop while purchase != to 'no'
#1.9 1 Display trader items with prices
#1.9.2 Ask user to buy items
#1.9.3 if trader has enough gold and item in stock, buy item  
#1.10 Introduce another player
## Combat section
# Prepare the list with descriptions of text.
## hits = (), misses = (), damage_taken = (), health update = ()
#2 Players enter battle.
## Player decides which weapon to use.
## As long as weapon is in inventory to use.
## If weapon doesnt exist, the player will use his fists.
#3 Loop while oppenent [health] > 0 and target [health] > 0:
#3.1 for player in battle:
#3.1.1 Calculate ther attack speen
#3.1.2 Calulate the attack damage
#3.1.3 Print damage taken
#3.1.4 if opponent [health] > 0 and target [health] > 0:
#break
#3.2 Print player progress
#4 Print Winner