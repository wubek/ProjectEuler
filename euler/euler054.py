# author wukat
'''
In the card game poker, a hand consists of five cards and are 
ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the 
highest value wins; for example, a pair of eights beats a pair of fives 
(see example 1 below). But if two ranks tie, for example, both players 
have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest 
cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	Player 1	 		Player 2	 	Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD  Player 2
		Pair of Fives 		Pair of Eights

2	 	5D 8C 9S JS AC 		2C 5C 7D 8S QH 	Player 1
		Highest card Ace 	Highest card Queen
 	
3	 	2D 9C AS AH AC 		3D 6D 7D TD QD 	Player 2
		Three Aces 			Flush with Diamonds
 	
4	 	4D 6S 9H QH QC 		3D 6D 7H QD QS 	Player 1
		Pair of Queens		Pair of Queens
		Highest card Nine 	Highest card Seven

5	 	2H 2D 4C 4D 4S 		3C 3D 3S 9S 9D 	Player 1
		Full House 			Full House
		With Three Fours	with Three Threes	
 	 	
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

def evaluate_card(card):
	char = card[0]
	if char <= "9" and char >= "0":
		return ord(char) - ord("0")
	elif char == "T":
		return 10
	elif char == "J":
		return 11
	elif char == "Q":
		return 12
	elif char  == "K":
		return 13
	else:
		return 14

def compare_cards(first_card, second_card):
	return evaluate_card(first_card) > evaluate_card(second_card)

def make_occurances_dict(values):
	occurances = {}
	for i in values:
		if i in occurances:
			occurances[i] += 1
		else:
			occurances[i] = 1
	return occurances

def is_flush(cards):
	'''Flush: All cards of the same suit.'''
	color = cards[0][1]
	for i in cards[1:]:
		if i[1] != color:
			return False
	return max(map(lambda card: evaluate_card(card), cards))

def is_straight(cards):
	'''Straight: All cards are consecutive values.'''
	values = map(lambda card: evaluate_card(card), cards)
	min_val = min(values)
	for i in range(1,5):
		if not min_val + i in values:
			return False
	return min_val + 4

def is_straight_flush(cards):
	'''Straight Flush: All cards are consecutive values of same suit.'''
	if is_flush(cards):
		return is_straight(cards)

def is_four_of_kind(occurances):
	'''Four of a Kind: Four cards of the same value.'''
	for card, occs in occurances.items():
		if occs >= 4:
			return card

def is_full_house(occurances):
	'''Full House: Three of a kind and a pair.'''
	if len(occurances) == 2:
		for card, occ in occurances.items():
			if occ == 2 or occ == 3:
				return max(occurances.keys()) 

def is_thrre_of_kind(occurances):
	'''Three of a Kind: Three cards of the same value.'''
	if len(occurances) == 3:
		for card, occ in occurances.items():
			if occ == 3:
				return card

def is_two_pairs(occurances):
	'''Two Pairs: Two different pairs. Works if we know that it's not 3 of kind '''
	pairs = []
	if len(occurances) == 3:
		for card, occ in occurances.items():
			if occ == 2:
				pairs.append(card)
		return max(pairs)

def is_pair(occurances):
	'''Two Pairs: Two different pairs. Works if we know that it's not 3 of kind '''
	if len(occurances) == 4:
		for card, occ in occurances.items():
			if occ == 2:
				return card

def evaluate_hand(cards):
	occurances = make_occurances_dict(map(lambda card: evaluate_card(card), cards))
	if len(occurances) == 5:
		if min(occurances.keys()) == 10:
			return 9 * 20 # royal_flush
		else:
			val = is_straight_flush(cards)
			if val:
				return val + 8 * 20
	val = is_four_of_kind(occurances)
	if val:
		return val + 7 * 20
	val = is_full_house(occurances)
	if val:
		return val + 6 * 20
	val = is_flush(cards)
	if val:
		return val + 5 * 20
	val = is_straight(cards)
	if val:
		return val + 4 * 20
	val = is_thrre_of_kind(occurances)
	if val:
		return val + 3 * 20
	val = is_two_pairs(occurances)
	if val:
		return val + 2 * 20
	val = is_pair(occurances)
	if val:
		return val + 20
	return max(occurances.keys())

def play_poker(first_pl, second_pl):
	if evaluate_hand(first_pl) > evaluate_hand(second_pl):
		return 1
	return 0

if __name__ == '__main__':
	count_player_1 = 0
	with open("euler054.input", "r") as input_cards:
		for line in input_cards:
			count_player_1 += play_poker(line.split()[0:5], line.split()[5:10])
	print(count_player_1)