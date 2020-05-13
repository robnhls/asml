import deck
import unittest

class test_deck(unittest.TestCase):

    def setUp(self):
        self.cards = deck.getcards()


    def test_52_cards(self):
        # AAA Pattern

        # Arrange
        EXPECTED_COUNT = 52

        # Act
        
        count = len(self.cards)

        # Assert
        self.assertEqual(count, EXPECTED_COUNT)

    def test_13_hearts(self):

        HEART_COUNT = 13
        suit = deck.HEARTS

        
        count = 0
        for card in self.cards:
            if card[1] == suit:
                count += 1
        
        self.assertEqual(HEART_COUNT, count)


if __name__ == '__main__':
    unittest.main()