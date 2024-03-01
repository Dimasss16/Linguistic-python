import unittest

from xbar import *


class TestTask1(unittest.TestCase):

    ############
    # Setup
    ############

    def setUp(self):
        self.book = Tree('Book', [
            Tree('Chapter 1', [Tree('Section 1.1'), Tree('Section 1.2')]),
            Tree('Chapter 2', [Tree('Section 2.1', [Tree('Subsection 2.1.1'), Tree('Subsection 2.1.2')])]),
            Tree('Chapter 3')
        ])

        self.book_preorder = ['Book',
                     'Chapter 1', 'Section 1.1', 'Section 1.2',
                     'Chapter 2', 'Section 2.1', 'Subsection 2.1.1', 'Subsection 2.1.2',
                     'Chapter 3']
        self.book_postorder = ['Section 1.1', 'Section 1.2', 'Chapter 1',
                      'Subsection 2.1.1', 'Subsection 2.1.2', 'Section 2.1', 'Chapter 2',
                      'Chapter 3',
                      'Book']

    ############
    # Traversals
    ############

    # Preorder

    def test_preorder1(self):
        self.assertEqual(Tree.names(self.book.preorder())[:4], self.book_preorder[:4])

    def test_preorder2(self):
        self.assertEqual(Tree.names(self.book.preorder()), self.book_preorder)

    # Postorder

    def test_postorder1(self):
        self.assertEqual(Tree.names(self.book.postorder())[:4], self.book_postorder[:4])

    def test_postorder2(self):
        self.assertEqual(Tree.names(self.book.postorder()), self.book_postorder)


class TestTask2(unittest.TestCase):

    ############
    # Setup
    ############

    def setUp(self):
        self.cat_terminal = Tree('cat')
        self.cat_N = Tree('N0', [self.cat_terminal])
        self.cat_Nbar = Tree('N1', [self.cat_N])
        self.cat_NP = Tree('N2', [self.cat_Nbar])
        self.the = Tree('D2', [Tree('D1', [Tree('D0', [Tree('the')])])])

        self.the_cat = Tree('N2', [self.the, self.cat_Nbar])

        self.small_cat = Tree('N1',
                              [Tree('A2', [Tree('A1', [Tree('A0', [Tree('small')])])]),
                               self.cat_Nbar
                               ])  # adjunct

        self.small_black_cat = Tree('N1',
                                    [Tree('A2', [Tree('A1', [Tree('A0', [Tree('small')])])]),
                                     Tree('N1',
                                          [Tree('A2', [Tree('A1', [Tree('A0', [Tree('black')])])]),
                                           self.cat_Nbar
                                           ])
                                     ])  # iteration of adjuncts

        self.on_the_mat_Pbar = Tree('P1',
                                    [Tree('P0', [Tree('on')]),
                                     Tree('N2', [self.the,
                                                 Tree('N1', [Tree('N0', [Tree('mat')])])])])  # complement

        self.on_the_mat = Tree('P2', [self.on_the_mat_Pbar])  # complement

        self.cat_on_the_mat = Tree('N1', [self.cat_Nbar, self.on_the_mat])  # adjunct

        self.the_cat_on_the_mat = Tree('N2', [self.the, self.cat_on_the_mat])  # ajdunct

        self.quickly = Tree('Adv2', [Tree('Adv1', [Tree('Adv0', [Tree('quickly')])])])  # len(category) > 1

        self.cat_wrong_no_N1 = Tree('N2', [self.the, self.cat_N])  # no N' level
        self.cat_wrong_two_N1 = Tree('N2', [Tree('N1', [self.cat_Nbar])])  # one N' level too many
        self.cat_wrong_category_mismatch = Tree('P2', [self.the, Tree('N1', [
            self.cat_N])])  # categories of phrase and bar don't match
        self.cat_wrong_two_heads = Tree('N1', [self.cat_N, self.cat_N])  # two heads

    ############
    # Projection levels
    ############

    # Phrase    # already implemented

    def test_is_phrase_projection1(self):
        self.assertTrue(self.cat_NP.is_phrase_projection())

    def test_is_phrase_projection2(self):
        self.assertFalse(self.cat_wrong_category_mismatch.is_phrase_projection())
        self.assertFalse(self.cat_wrong_no_N1.is_phrase_projection())

    # Bar

    def test_is_bar_projection1(self):
        self.assertTrue(self.cat_Nbar.is_bar_projection())

    def test_is_bar_projection2(self):
        self.assertFalse(self.cat_NP.is_bar_projection())
        self.assertFalse(self.cat_wrong_two_heads.is_bar_projection())

    # Head

    def test_is_head_projection1(self):
        self.assertTrue(self.cat_N.is_head_projection())

    def test_is_head_projection2(self):
        self.assertFalse(self.cat_terminal.is_head_projection())
        self.assertFalse(self.cat_Nbar.is_head_projection())

    ############
    # Structural constraints
    ############

    # No specifier

    def test_is_no_specifier_structure1(self):
        self.assertTrue(self.cat_NP.is_no_specifier_structure())

    def test_is_no_specifier_structure2(self):
        self.assertFalse(self.the_cat.is_no_specifier_structure())

    # Specifier

    def test_is_specifier_structure1(self):
        self.assertTrue(self.the_cat.is_specifier_structure())

    def test_is_specifier_structure2(self):
        self.assertFalse(self.cat_NP.is_specifier_structure())

    # No adjunct or complement

    def test_is_no_adjunct_or_complement_structure1(self):
        self.assertTrue(self.cat_Nbar.is_no_adjunct_or_complement_structure())

    def test_is_no_adjunct_or_complement_structure2(self):
        self.assertFalse(self.on_the_mat_Pbar.is_no_adjunct_or_complement_structure())

    # Complement    # already implemented

    def test_is_complement_structure1(self):
        self.assertTrue(self.on_the_mat_Pbar.is_complement_structure())

    def test_is_complement_structure2(self):
        self.assertFalse(self.cat_on_the_mat.is_complement_structure())

    # Adjunct

    def test_is_adjunct_structure1(self):
        self.assertTrue(self.cat_on_the_mat.is_adjunct_structure())
        self.assertTrue(self.small_black_cat.is_adjunct_structure())

    def test_is_adjunct_structure2(self):
        self.assertFalse(self.on_the_mat_Pbar.is_adjunct_structure())

    # Head

    def test_is_head_structure1(self):
        self.assertTrue(self.cat_N.is_head_structure())

    def test_is_head_structure2(self):
        self.assertFalse(self.cat_terminal.is_head_structure())


if __name__ == '__main__':
    unittest.main()
