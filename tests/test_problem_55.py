import unittest

from problem_55 import is_palindrome, reverse_num, Lychrel

class TestIsPalindrome(unittest.TestCase):

    def test_string_odd_length(self):
        self.assertTrue(is_palindrome('tacocat'))
        self.assertFalse(is_palindrome('hello'))
    
    def test_string_even_length(self):
        self.assertTrue(is_palindrome('anna'))
        self.assertFalse(is_palindrome('alcclo'))

    def test_num_odd_length(self):
        self.assertTrue(is_palindrome(12345678987654321))
        self.assertFalse(is_palindrome(1234121))
    
    def test_num_even_length(self):
        self.assertTrue(is_palindrome(12345678900987654321))
        self.assertFalse(is_palindrome(123456653421))
    

class TestReverseNum(unittest.TestCase):

    def test_reverse_even_length(self):
        self.assertEqual(reverse_num(1234), 4321)
        self.assertEqual(reverse_num(1000), 1)

    def test_reverse_odd_length(self):
        self.assertEqual(reverse_num(12345), 54321)
        self.assertEqual(reverse_num(5), 5)
    

class TestIsLychrel(unittest.TestCase):
    
    lychrel = Lychrel(50)

    def test_lychrel(self):
        self.assertTrue(self.lychrel.is_lychrel(196))
        self.assertTrue(self.lychrel.is_lychrel(4994))
    
    def test_not_lychrel(self):
        self.assertFalse(self.lychrel.is_lychrel(99))
        self.assertFalse(self.lychrel.is_lychrel(349))
        self.assertFalse(self.lychrel.is_lychrel(3223))