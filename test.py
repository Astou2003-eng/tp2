import unittest
from fizz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_intervalle(self):
        result = affiche(5, 10)
        expected = 'BuzzFizz78FizzBuzz'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
