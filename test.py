from pokerHandCounter import *

# Has a royal flush
hand1 = [Card(Suit.CLUBS, Face.ACE),
		 Card(Suit.CLUBS, Face.JACK),
		 Card(Suit.CLUBS, Face.QUEEN),
		 Card(Suit.CLUBS, Face.KING),
		 Card(Suit.CLUBS, Face.TEN)]
assert allSameSuit(hand1)
assert isRoyalFlush(hand1)

# Mismatched suit
hand2 = [Card(Suit.CLUBS, Face.ACE),
		 Card(Suit.HEARTS, Face.JACK),
		 Card(Suit.CLUBS, Face.QUEEN),
		 Card(Suit.CLUBS, Face.KING),
		 Card(Suit.CLUBS, Face.TEN)]
assert not allSameSuit(hand2)
assert not isRoyalFlush(hand2)

# Not flush cards
hand3 = [Card(Suit.CLUBS, Face.ACE),
		 Card(Suit.CLUBS, Face.JACK),
		 Card(Suit.CLUBS, Face.TEN),
		 Card(Suit.CLUBS, Face.KING),
		 Card(Suit.CLUBS, Face.TEN)]
assert allSameSuit(hand3)
assert not isRoyalFlush(hand3)

# Testing the card Rankings
hand4 = [Card(Suit.CLUBS, Face.TWO),
		 Card(Suit.CLUBS, Face.THREE),
		 Card(Suit.CLUBS, Face.FOUR),
		 Card(Suit.CLUBS, Face.FIVE),
		 Card(Suit.CLUBS, Face.SIX)]
rankings = transformHandToCardRankings(hand4)
assert rankings == [2, 3, 4, 5, 6]
assert getLongestSequence(hand4) == [2, 3, 4, 5, 6]

hand5 = [Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.EIGHT),
		 Card(Suit.CLUBS, Face.TEN),
		 Card(Suit.CLUBS, Face.JACK),
		 Card(Suit.CLUBS, Face.ACE)]
rankings = transformHandToCardRankings(hand5)
assert rankings == [7, 8, 10, 11, 14]
assert getLongestSequence(hand5) == [7, 8]

hand6 = [Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.EIGHT),
		 Card(Suit.CLUBS, Face.SIX),
		 Card(Suit.CLUBS, Face.FIVE),
		 Card(Suit.CLUBS, Face.FOUR)]
rankings = transformHandToCardRankings(hand6)
assert isStraightFlush(hand6)

hand7 = [Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.FIVE),
		 Card(Suit.CLUBS, Face.FOUR)]
assert not isFullHouse(hand7)

hand8 = [Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.FIVE)]
assert not isFullHouse(hand8)

hand9 = [Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.SEVEN),
		 Card(Suit.CLUBS, Face.FIVE),
		 Card(Suit.CLUBS, Face.FIVE)]
assert isFullHouse(hand9)

# Test the card level
royalFlush = [Card(Suit.CLUBS, Face.ACE),
			  Card(Suit.CLUBS, Face.JACK),
			  Card(Suit.CLUBS, Face.QUEEN),
			  Card(Suit.CLUBS, Face.KING),
			  Card(Suit.CLUBS, Face.TEN)]
CL1 = CardHand(royalFlush)

straightFlush = [Card(Suit.CLUBS, Face.NINE),
				 Card(Suit.CLUBS, Face.JACK),
				 Card(Suit.CLUBS, Face.QUEEN),
				 Card(Suit.CLUBS, Face.KING),
				 Card(Suit.CLUBS, Face.TEN)]
CL2 = CardHand(straightFlush)
assert CL2.level == Level.STRAIGHTFLUSH

fourOfAKind = [Card(Suit.CLUBS, Face.NINE),
			   Card(Suit.HEARTS, Face.NINE),
			   Card(Suit.SPADES, Face.NINE),
			   Card(Suit.DIAMONDS, Face.NINE),
			   Card(Suit.CLUBS, Face.TEN)]
CL3 = CardHand(fourOfAKind)
assert CL3.level == Level.FOUROFAKIND

fullHouse = [Card(Suit.CLUBS, Face.NINE),
			 Card(Suit.HEARTS, Face.NINE),
			 Card(Suit.SPADES, Face.NINE),
			 Card(Suit.DIAMONDS, Face.TEN),
			 Card(Suit.CLUBS, Face.TEN)]
CL4 = CardHand(fullHouse)
assert CL4.level == Level.FULLHOUSE

flush = [Card(Suit.CLUBS, Face.NINE),
		 Card(Suit.CLUBS, Face.ACE),
		 Card(Suit.CLUBS, Face.JACK),
		 Card(Suit.CLUBS, Face.KING),
		 Card(Suit.CLUBS, Face.TWO)]
CL5 = CardHand(flush)
assert CL5.level == Level.FLUSH

straight = [Card(Suit.CLUBS, Face.NINE),
			Card(Suit.HEARTS, Face.TEN),
			Card(Suit.DIAMONDS, Face.JACK),
			Card(Suit.SPADES, Face.KING),
			Card(Suit.CLUBS, Face.QUEEN)]
CL6 = CardHand(straight)
assert CL6.level == Level.STRAIGHT

threeOfAKind = [Card(Suit.CLUBS, Face.TEN),
				Card(Suit.HEARTS, Face.TEN),
				Card(Suit.DIAMONDS, Face.TEN),
				Card(Suit.SPADES, Face.KING),
				Card(Suit.CLUBS, Face.QUEEN)]
CL7 = CardHand(threeOfAKind)
assert CL7.level == Level.THREEOFAKIND

twoPairs = [Card(Suit.CLUBS, Face.TEN),
			Card(Suit.HEARTS, Face.TEN),
			Card(Suit.DIAMONDS, Face.NINE),
			Card(Suit.SPADES, Face.KING),
			Card(Suit.CLUBS, Face.KING)]
CL8 = CardHand(twoPairs)
assert CL8.level == Level.TWOPAIRS

pair = [Card(Suit.CLUBS, Face.TEN),
		Card(Suit.HEARTS, Face.TEN),
		Card(Suit.DIAMONDS, Face.ACE),
		Card(Suit.SPADES, Face.THREE),
		Card(Suit.CLUBS, Face.FIVE)]
CL9 = CardHand(pair)
assert CL9.level == Level.PAIR

highCard = [Card(Suit.DIAMONDS, Face.THREE),
			Card(Suit.SPADES, Face.JACK),
			Card(Suit.DIAMONDS, Face.EIGHT),
			Card(Suit.HEARTS, Face.FOUR),
			Card(Suit.CLUBS, Face.TWO)]
CL10 = CardHand(highCard)
assert CL10.level == Level.HIGHCARD

# Assert comparison operators
assert CL1.isGreaterThan(CL2)
assert CL2.isGreaterThan(CL3)
assert CL3.isGreaterThan(CL4)
assert CL4.isGreaterThan(CL5)
assert CL5.isGreaterThan(CL6)
assert CL6.isGreaterThan(CL7)
assert CL7.isGreaterThan(CL8)
assert CL8.isGreaterThan(CL9)
assert CL9.isGreaterThan(CL10)
assert CL1.isEqualTo(CL1)
assert CL2.isEqualTo(CL2)
assert CL3.isEqualTo(CL3)
assert CL4.isEqualTo(CL4)
assert CL5.isEqualTo(CL5)
assert CL6.isEqualTo(CL6)
assert CL7.isEqualTo(CL7)
assert CL8.isEqualTo(CL8)
assert CL9.isEqualTo(CL9)
assert CL10.isEqualTo(CL10)
# TEST SORTING
sort = sortHands([CL10, CL8, CL2, CL3, CL4, CL6, CL7, CL1, CL5, CL1, CL1, CL1, CL9])
expectedSorted = [Level.ROYALFLUSH,
				  Level.ROYALFLUSH,
				  Level.ROYALFLUSH,
				  Level.ROYALFLUSH,
				  Level.STRAIGHTFLUSH,
				  Level.FOUROFAKIND,
				  Level.FULLHOUSE,
				  Level.FLUSH,
				  Level.STRAIGHT,
				  Level.THREEOFAKIND,
				  Level.TWOPAIRS,
				  Level.PAIR,
				  Level.HIGHCARD]
for i in range(0, len(sort)):
	assert sort[i].level == expectedSorted[i]

# Testing Equality on Royal Flushs
royalFlush = [Card(Suit.CLUBS, Face.ACE),
			  Card(Suit.CLUBS, Face.JACK),
			  Card(Suit.CLUBS, Face.QUEEN),
			  Card(Suit.CLUBS, Face.KING),
			  Card(Suit.CLUBS, Face.TEN)]
CL1 = CardHand(royalFlush)
CL2 = CardHand(royalFlush)
assert CL1.isEqualTo(CL2)
assert not CL1.isGreaterThan(CL2)

# Testing equality on straight flush
straightFlush = [Card(Suit.CLUBS, Face.NINE),
				 Card(Suit.CLUBS, Face.JACK),
				 Card(Suit.CLUBS, Face.QUEEN),
				 Card(Suit.CLUBS, Face.KING),
				 Card(Suit.CLUBS, Face.TEN)]
CL1 = CardHand(straightFlush)
straightFlush = [Card(Suit.CLUBS, Face.EIGHT),
				 Card(Suit.CLUBS, Face.NINE),
				 Card(Suit.CLUBS, Face.TEN),
				 Card(Suit.CLUBS, Face.JACK),
				 Card(Suit.CLUBS, Face.QUEEN)]
CL2 = CardHand(straightFlush)
assert CL1.isGreaterThan(CL2)
assert not CL1.isEqualTo(CL2)

# Test equality on two pairs
twoPairs = [Card(Suit.CLUBS, Face.FOUR),
			Card(Suit.HEARTS, Face.FOUR),
			Card(Suit.DIAMONDS, Face.THREE),
			Card(Suit.SPADES, Face.THREE),
			Card(Suit.CLUBS, Face.KING)]
CL1 = CardHand(twoPairs)
twoPairs = [Card(Suit.CLUBS, Face.FOUR),
			Card(Suit.HEARTS, Face.FOUR),
			Card(Suit.DIAMONDS, Face.TWO),
			Card(Suit.SPADES, Face.TWO),
			Card(Suit.CLUBS, Face.KING)]
CL2 = CardHand(twoPairs)
assert CL1.isGreaterThan(CL2)
assert not CL1.isEqualTo(CL2)
twoPairs = [Card(Suit.CLUBS, Face.FOUR),
			Card(Suit.HEARTS, Face.FOUR),
			Card(Suit.DIAMONDS, Face.THREE),
			Card(Suit.SPADES, Face.THREE),
			Card(Suit.CLUBS, Face.KING)]
CL2 = CardHand(twoPairs)
assert not CL1.isGreaterThan(CL2)
assert CL1.isEqualTo(CL2)

twoPairs = [Card(Suit.CLUBS, Face.FOUR),
			Card(Suit.HEARTS, Face.FOUR),
			Card(Suit.DIAMONDS, Face.THREE),
			Card(Suit.SPADES, Face.THREE),
			Card(Suit.CLUBS, Face.QUEEN)]
CL2 = CardHand(twoPairs)
assert CL1.isGreaterThan(CL2)
assert not CL1.isEqualTo(CL2)