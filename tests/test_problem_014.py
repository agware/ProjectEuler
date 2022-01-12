import unittest

from problem_014 import Collatz

class TestProblem014(unittest.TestCase):

    def test_get_length_single(self):
        self.assertEqual(Collatz().get_length(-1), 0)
        self.assertEqual(Collatz().get_length(1), 1)
        self.assertEqual(Collatz().get_length(4), 3)
        self.assertEqual(Collatz().get_length(20), 8)

    def test_get_length_multiple(self):
        collatz = Collatz()

        self.assertEqual(collatz.get_length(-1), 0)
        self.assertEqual(collatz.get_length(1), 1)
        self.assertEqual(collatz.get_length(4), 3)
        self.assertEqual(collatz.get_length(20), 8)

    def test_get_longest_single(self):
        collatz = Collatz()
        _ = collatz.get_length(13)

        self.assertEqual(collatz.get_longest_root(), 13)
        self.assertEqual(collatz.get_longest_length(), 10)

    def test_get_longest_multiple(self):
        collatz = Collatz()

        for i in range(1,5):
            _ = collatz.get_length(i)
        
        self.assertEqual(collatz.get_longest_root(), 3)
        self.assertEqual(collatz.get_longest_length(), 8)