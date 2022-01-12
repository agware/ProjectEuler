import unittest

from problem_15 import Lattice

class TestProblem15(unittest.TestCase):

    def test_one_square(self):
        lattice = Lattice(1)
        self.assertEqual(lattice.get_moves_required(0, 0), 2)

    def test_two_squares(self):
        lattice = Lattice(2)
        self.assertEqual(lattice.get_moves_required(0, 0), 6)