import unittest
from fizz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_base(self):
        result = affiche()
        expected = '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz...9798FizzBuzz'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
