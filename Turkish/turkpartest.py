import unittest
from turkpar import *


# tests for the Task 1
class TestTask1(unittest.TestCase):

    def test_is_vowel(self):
        self.assertEqual(True, is_vowel("e"))
        self.assertEqual(False, is_vowel("k"))


# tests for Task 2
class TestTask2(unittest.TestCase):

    def test_ends_in_vowel(self):
        self.assertEqual(True, ends_in_vowel("su"))
        self.assertEqual(False, ends_in_vowel("un"))


# tests for Task 3
class TestTask3(unittest.TestCase):

    def test_get_last_vowel(self):
        self.assertEqual(None, get_last_vowel("trp"))
        self.assertEqual("a", get_last_vowel("orta"))
        self.assertEqual("u", get_last_vowel("kurt"))


# tests for Task 4
class TestTask4(unittest.TestCase):

    def test_is_voiced(self):
        self.assertEqual(True, is_voiced("ğ"))
        self.assertEqual(False, is_voiced("a"))


# tests for Task 5
class TestTask5(unittest.TestCase):

    def test_major_vowel_harmony(self):
        self.assertEqual("ü", i_type_harmony("ö"))
        self.assertEqual("ı", i_type_harmony("ı"))
        self.assertEqual(None, i_type_harmony("k"))


# tests for Task 6
class TestTask6(unittest.TestCase):

    def test_a_type_vowel_harmony(self):
        self.assertEqual("e", a_type_harmony("ö"))
        self.assertEqual("a", a_type_harmony("ı"))
        self.assertEqual(None, a_type_harmony("k"))


# tests for Task 7
class TestTask7(unittest.TestCase):

    def test_consonant_shift(self):
        self.assertEqual("d", consonant_harmony("deniz"))
        self.assertEqual("t", consonant_harmony("bulut"))


# tests for Task 8
class TestTask8(unittest.TestCase):

    def test_inflect_noun(self):
        self.assertEqual("memleket", inflect_noun("memleket", "NOM", "singular"))
        self.assertEqual("memleketleri", inflect_noun("memleket", "ACC", "plural"))
        self.assertEqual("ülkeyin", inflect_noun("ülke", "GEN", "singular"))
        self.assertEqual("adamlardan", inflect_noun("adam", "ABL", "plural"))


if __name__ == '__main__':
    unittest.main()
