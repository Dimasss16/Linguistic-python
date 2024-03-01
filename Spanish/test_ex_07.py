import unittest
from ex_07 import *

file_name = "spanish-tagged-spacy.txt"

class TestTask1(unittest.TestCase):

    def setUp(self):
        self.sentences = load_sentences(file_name)

    # Test 1: successful processing
    def test_load_sentences1(self):
        self.assertNotEqual(self.sentences, None)

    # Test 2: result is a list of correct size
    def test_load_sentences2(self):
        self.assertIsInstance(self.sentences, type(list()))
        self.assertEqual(len(self.sentences), 71201)

    # Test 3: each sentence is a list of tuples of length 2
    def test_load_sentences3(self):
        self.assertIsInstance(self.sentences[0], type(list()))
        self.assertIsInstance(self.sentences[0][0], type(tuple()))
        self.assertEqual(len(self.sentences[0][0]), 2)

    # Test 4: sentences have the correct number of tokens
    def test_load_sentences4(self):
        self.assertEqual(len(self.sentences[0]), 6)
        self.assertEqual(len(self.sentences[1]), 9)

    # Test 5: first elements of tuples contain the words:
    def test_load_sentences5(self):
        self.assertEqual(self.sentences[0][0][0], "No")
        self.assertEqual(self.sentences[0][1][0], ",")
        self.assertEqual(self.sentences[2][0][0], "¿")
        self.assertEqual(self.sentences[2][1][0], "Qué")

    # Test 6: second elements of tuples contain the tags:
    def test_load_sentences6(self):
        self.assertEqual(self.sentences[0][0][1], "ADV")
        self.assertEqual(self.sentences[0][1][1], "PUNCT")
        self.assertEqual(self.sentences[2][0][1], "PUNCT")
        self.assertEqual(self.sentences[2][1][1], "PRON")


class TestTask2(unittest.TestCase):

    # Test 7: no change for forms ending in -o
    def test_lemmatize1(self):
        self.assertEqual(lemmatize("pequeño"), "pequeño")

    # Test 8: normalize adjectives in -a to -o
    def test_lemmatize2(self):
        self.assertEqual(lemmatize("pequeña"), "pequeño")

    # Test 9: normalize adjectives in -os to -o
    def test_lemmatize3(self):
        self.assertEqual(lemmatize("pequeños"), "pequeño")

    # Test 10: normalize adjectives in -as to -o
    def test_lemmatize4(self):
        self.assertEqual(lemmatize("pequeñas"), "pequeño")

    # Test 11: normalize adjectives in -ces to -z
    def test_lemmatize5(self):
        self.assertEqual(lemmatize("capaces"), "capaz")

    # Test 12: normalize adjectives in -és
    def test_lemmatize6(self):
        self.assertEqual(lemmatize("ingleses"), "inglés")
        self.assertEqual(lemmatize("inglesa"), "inglés")
        self.assertEqual(lemmatize("inglesas"), "inglés")

    # Test 13: normalize to -nte/-ble/-bre/-nse
    def test_lemmatize7(self):
        self.assertEqual(lemmatize("interesantes"), "interesante")
        self.assertEqual(lemmatize("agradables"), "agradable")
        self.assertEqual(lemmatize("libres"), "libre")
        self.assertEqual(lemmatize("canadienses"), "canadiense")

    # Test 14: normalize to -l/-r/-n
    def test_lemmatize8(self):
        self.assertEqual(lemmatize("iguales"), "igual")
        self.assertEqual(lemmatize("lanares"), "lanar")

    # Test 15: normalize other adjectives in -es to -e
    def test_lemmatize9(self):
        self.assertEqual(lemmatize("tristes"), "triste")
        self.assertEqual(lemmatize("grandes"), "grande")

    # Test 16: no change for other forms
    def test_lemmatize10(self):
        self.assertEqual(lemmatize("capaz"), "capaz")
        self.assertEqual(lemmatize("inglés"), "inglés")
        self.assertEqual(lemmatize("igual"), "igual")


class TestTask3(unittest.TestCase):

    def setUp(self):
        self.sentences = load_sentences(file_name)
        self.freq_ser, self.freq_estar = count_occurrences(self.sentences)
   
    # Test 17: successful processing
    def test_count_occurrences1(self):
        self.assertNotEqual(self.freq_ser, None)
        self.assertNotEqual(self.freq_estar, None)

    # Test 18: both maps have the same number of keys
    def test_count_occurrences2(self):
        self.assertEqual(len(self.freq_ser), len(self.freq_estar))
        
    # Test 19: keys are strings
    def test_count_occurrences3(self):
        self.assertIsInstance(next(iter(self.freq_ser.keys())), type(""))
        self.assertIsInstance(next(iter(self.freq_estar.keys())), type(""))

    # Test 20: values are integers
    def test_count_occurrences4(self):
        self.assertIsInstance(next(iter(self.freq_ser.values())), type(1))
        self.assertIsInstance(next(iter(self.freq_estar.values())), type(1))

    # Test 21: correct counts in freq_ser
    def test_count_occurrences5(self):
        self.assertEqual(self.freq_ser["diferente"], 94)
        self.assertEqual(self.freq_ser["amarillo"], 34)

    # Test 22: correct counts in freq_estar
    def test_count_occurrences6(self):
        self.assertEqual(self.freq_estar["acostado"], 10)
        self.assertEqual(self.freq_estar["parado"], 65)

    # Test 23: first keys in alphabetical order are identical and correct
    def test_count_occurrences7(self):
        self.assertEqual(sorted(self.freq_ser.keys())[0:5], sorted(self.freq_estar.keys())[0:5])
        sorted_list = sorted(self.freq_ser.keys())
        self.assertEqual(sorted_list[2],"abandonado")
        self.assertEqual(sorted_list[3],"abarrotado")
        self.assertEqual(sorted_list[4],"abducido")

    # Test 24: zero counts in the respective other frequency dictionary
    def test_count_occurrences8(self):
        self.assertEqual(self.freq_ser["fundido"], 0)
        self.assertEqual(self.freq_ser["adornado"], 0)
        self.assertEqual(self.freq_estar["inaccesible"], 0)
        self.assertEqual(self.freq_estar["inglés"], 0)

class TestTask4(unittest.TestCase):

    def setUp(self):
        self.sentences = load_sentences(file_name)
        self.freq_ser, self.freq_estar = count_occurrences(self.sentences)
        self.ser, self.estar, self.both = get_occurrence_sets(self.freq_ser, self.freq_estar)

    # Test 25: successful processing
    def test_get_occurrence_sets1(self):
        self.assertNotEqual(self.ser, None)
        self.assertNotEqual(self.estar, None)
        self.assertNotEqual(self.both, None)

    # Test 26: all three results are sets
    def test_get_occurrence_sets2(self):
        self.assertIsInstance(self.ser, type(set()))
        self.assertIsInstance(self.estar, type(set()))
        self.assertIsInstance(self.both, type(set()))

    # Test 27: no overlap between the three sets
    def test_get_occurrence_sets3(self):
        self.assertEqual(len(self.ser & self.estar), 0)
        self.assertEqual(len(self.ser & self.both), 0)
        self.assertEqual(len(self.both & self.estar), 0)

    # Test 28: clear cases in self.ser
    def test_get_occurrence_sets4(self):
        self.assertIn("pobre", self.ser)
        self.assertIn("lindo", self.ser)

    # Test 29: clear cases in self.estar
    def test_get_occurrence_sets5(self):
        self.assertIn("ocupado", self.estar)
        self.assertIn("vivo", self.estar)  

    # Test 30: clear cases in self.both
    def test_get_occurrence_sets6(self):
        self.assertIn("bueno", self.both)
        self.assertIn("bajo", self.both)

    # Test 31: correct sizes of sets
    def test_get_occurrence_sets7(self):
        self.assertEqual(len(self.ser), 152)
        self.assertEqual(len(self.estar), 90)
        self.assertEqual(len(self.both), 87)

    # Test 32: boundary cases (e.g. = 10 and < 10 overall, 1 to 9)
    def test_get_occurrence_sets8(self):
        self.assertIn("típico", self.ser)
        self.assertIn("feo", self.both)
        self.assertIn("abierto", self.both)

if __name__ == '__main__':
    unittest.main()