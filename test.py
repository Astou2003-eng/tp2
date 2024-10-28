import unittest
from fizz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_param(self):
        result = affiche(15)
        expected = '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
