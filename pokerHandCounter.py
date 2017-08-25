from face import Face
from suit import Suit
from collections import Counter
from level import Level

cardRankings = {
	Face.ACE: 14,
	Face.TWO: 2,
	Face.THREE: 3,
	Face.FOUR: 4,
	Face.FIVE: 5,
	Face.SIX: 6,
	Face.SEVEN: 7,
	Face.EIGHT: 8,
	Face.NINE: 9,
	Face.TEN: 10,
	Face.JACK: 11,
	Face.QUEEN: 12,
	Face.KING: 13
}

# Simple card class to hold the main items of a card
class Card():
	def __init__(self, suit, face):
		self.suit = suit
		self.face = face

	def getRank(self):
		return cardRankings[self.face]

# The hand of cards, used for comparison between hands
class CardHand():
	def __init__(self, hand):
		copy = hand[:]
		self.hand = hand[:]
		self.level = self.getLevel(copy)
		self.comparisonValue = self.getComparisonValue(copy)

	def isGreaterThan(self, CardLevel2):
		if(self.level.value > CardLevel2.level.value):
			return True
		elif(self.level.value == CardLevel2.level.value):
			for cardIndex in range(0, len(self.comparisonValue)):
				if(self.comparisonValue[cardIndex] > CardLevel2.comparisonValue[cardIndex]):
					return True
			return False
		else:
			return False

	def isEqualTo(self, CardLevel2):
		if(self.level.value != CardLevel2.level.value):
			return False
		else:
			for cardIndex in range(0, len(self.comparisonValue)):
				if(self.comparisonValue[cardIndex] > CardLevel2.comparisonValue[cardIndex]):
					return False
			return True

	def getLevel(self, hand):
		if isRoyalFlush(hand):
			return Level.ROYALFLUSH
		elif isStraightFlush(hand):
			return Level.STRAIGHTFLUSH
		elif hasNumOfAKind(hand, 4):
			return Level.FOUROFAKIND
		elif isFullHouse(hand):
			return Level.FULLHOUSE
		elif isFlush(hand):
			return Level.FLUSH
		elif isStraight(hand):
			return Level.STRAIGHT
		elif hasNumOfAKind(hand, 3):
			return Level.THREEOFAKIND
		elif isTwoPairs(hand):
			return Level.TWOPAIRS
		elif isPair(hand):
			return Level.PAIR
		else:
			return Level.HIGHCARD

	def getComparisonValue(self, hand):
		ranks = transformHandToCardRankings(hand)
		if self.level == Level.FOUROFAKIND:
			quadruple = getLargestKind(hand)
			return quadruple + [x for x in ranks if x not in quadruple]
		elif self.level == Level.FULLHOUSE or self.level == Level.THREEOFAKIND:
			triple = getLargestKind(hand)
			return triple + [x for x in ranks if x not in triple]
		elif self.level == Level.TWOPAIRS:
			pair1 = getLargestKind(hand)
			pair1Faces = [getFaceFromRank(x) for x in pair1]
			for face in pair1Faces:
				removeCardFace(hand, face)
			pair2 = getLargestKind(hand)
			return sorted(pair1 + pair2, reverse=True) + [x for x in ranks if x not in (pair1 + pair2)]
		elif self.level == Level.PAIR:
			pair = getLargestKind(hand)
			pairFaces = [getFaceFromRank(x) for x in pair]
			for face in pairFaces:
				removeCardFace(hand, face)
			return pair + sorted(transformHandToCardRankings(hand), reverse=True)
		else:
			return sorted(transformHandToCardRankings(hand[:]), reverse=True)

# Given a rank, return the face (14 -> Ace)
def getFaceFromRank(rank):
	for face in cardRankings.keys():
		if cardRankings[face] == rank:
			return face

# Return true if a list of cards all have
def allSameSuit(hand):
	suit = hand[0].suit
	for card in hand:
		if card.suit != suit:
			return False
	return True

# Returns True if a hand has a certain card face
def hasCardFace(hand, cardFace):
	for card in hand:
		if card.face == cardFace:
			return True
	return False

# Deletes a face card from a hand, returns the new hand
def removeCardFace(hand, cardFace):
	for cardIndex in range(0, len(hand)):
		if hand[cardIndex].face == cardFace:
			del hand[cardIndex]
			return hand
	return hand

# Check to see if a hand contains the necessary cards for flush
def containsFlushCards(hand):
	flushFaces = [Face.ACE, Face.QUEEN, Face.JACK, Face.KING, Face.TEN]
	for f in flushFaces:
		if hasCardFace(hand, f) == False:
			return False
		else:
			hand = removeCardFace(hand, f)
	return True

# Check if a hand is a royal flush
def isRoyalFlush(hand):
	if allSameSuit(hand) and containsFlushCards(hand):
		return True
	else:
		return False

# Turn a list of a cards into a list of ranks [Ace, Queen] -> [14, 12]
def transformHandToCardRankings(hand):
	handRank = []
	for card in hand:
		handRank.append(card.getRank())
	return handRank

# Check if a hand is a flush
def isFlush(hand):
	if allSameSuit(hand):
		return True
	else:
		return False

# Check if hand is a straight flush
def isStraightFlush(hand):
	if allSameSuit(hand) and len(getLongestSequence(hand)) == 5:
		return True
	else:
		return False

# Return the rankings of the longest card sequence
def getLongestSequence(hand):
	rankings = transformHandToCardRankings(hand)
	rankings = sorted(rankings)
	longestSequence = [rankings[0]]
	currentSequence = [rankings[0]]
	for cardIndex in range(1, len(rankings)):
		if rankings[cardIndex] - rankings[cardIndex - 1] == 1:
			currentSequence.append(rankings[cardIndex])
			if (len(currentSequence) > len(longestSequence)):
				longestSequence = list(currentSequence)
		else:
			currentSequence = [rankings[cardIndex]]
	return longestSequence

# Check to see if a hand is a full house
def isFullHouse(hand):
	triplet = [getFaceFromRank(card) for card in getLargestKind(hand)]
	handCopy = list(hand)
	# Check for triple
	if len(triplet) != 3:
		return False
	for face in triplet:
		handCopy = removeCardFace(handCopy, face)
	couple = [getFaceFromRank(card) for card in getLargestKind(handCopy)]
	if len(couple) != 2:
		return False
	return True

# Check to see if a hand is a TwoOfAKind, ThreeOfAKind etc
def hasNumOfAKind(hand, num):
	if len(getLargestKind(hand)) == num:
		return True
	else:
		return False

# Check to see if a hand has 2 pairs
def isTwoPairs(hand):
	couple = [getFaceFromRank(card) for card in getLargestKind(hand)]
	handCopy = list(hand)
	# Check for triple
	if len(couple) != 2:
		return False
	for face in couple:
		handCopy = removeCardFace(handCopy, face)
	return isPair(handCopy)

# Check to see if a hand has a pair
def isPair(hand):
	couple = [getFaceFromRank(card) for card in getLargestKind(hand)]
	handCopy = list(hand)
	# Check for Couple
	if len(couple) != 2:
		return False
	else:
		return True

# Check to see if a hand is a straight
def isStraight(hand):
	if len(getLongestSequence(hand)) == 5:
		return True
	else:
		return False

# Get the largest group of a kind [Seven, Seven, Six] -> [7,7]
def getLargestKind(hand):
	rankings = transformHandToCardRankings(hand)
	rankings = sorted(rankings)
	count = Counter(rankings)
	maxFreq = 1
	currentKind = [count.values()[0] * count.keys()[0]]
	for k, v in count.items():
		if (v > maxFreq):
			maxFreq = v
			currentKind = [k] * v
	return currentKind

# Merge Sort for Card Hands
def sortHands(hands):
	if(len(hands) == 1):
		return hands
	else:
		hands1 = sortHands(hands[:len(hands)/2])
		hands2 = sortHands(hands[len(hands)/2:])
		return mergeHands(hands1, hands2)

# Merge Sort helper function
def mergeHands(hands1, hands2):
	merged = []
	while(len(hands1) != 0 and len(hands2) != 0):
		if(hands1[0].isGreaterThan(hands2[0])):
			merged.append(hands1[0])
			del hands1[0]
		elif(hands2[0].isGreaterThan(hands1[0])):
			merged.append(hands2[0])
			del hands2[0]
		else:
			merged.append(hands1[0])
			del hands1[0]
	# One of the lists is now empty, so they can be joined
	while(len(hands1) != 0):
		merged.append(hands1[0])
		del hands1[0]
	while(len(hands2) != 0):
		merged.append(hands2[0])
		del hands2[0]
	return merged