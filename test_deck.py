import deck
import unittest

class test_deck(unittest.TestCase):

    def test_52_cards(self):
        # AAA Pattern

        # Arrange
        EXPECTED_COUNT = 52

        # Act
        cards = deck.getcards()
        count = len(cards)

        # Assert
        self.assertEqual(count, EXPECTED_COUNT)

    def test_13_hearts(self):

        HEART_COUNT = 13
        suit = deck.HEARTS

        cards = deck.getcards()
        count = 0
        for card in cards:
            if card[1] == suit:
                count += 1
        
        self.assertEqual(HEART_COUNT, count)


if __name__ == '__main__':
    unittest.main()