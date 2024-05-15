import unittest
from app.sort import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    comb_sort,
    merge_sort,
    bucket_sort,
    cocktail_sort,
    gnome_sort,
    heap_sort,
    quick_sort,
    shell_sort,
)


class ordenacaoTestCase(unittest.TestCase):

    def setUp(self):
        self.a = [2, 1, 3, 5, 4]
        self.b = [1, 2, 3, 4, 5]

    @unittest.SkipTest
    def testando_bubble(self):
        self.assertListEqual(bubble_sort(self.a), self.b)

    @unittest.SkipTest
    def testando_selection(self):
        self.assertListEqual(selection_sort(self.a), self.b)

    @unittest.SkipTest
    def testando_insertion(self):
        self.assertListEqual(insertion_sort(self.a), self.b)

    @unittest.SkipTest
    def testando_comb(self):
        self.assertListEqual(comb_sort(self.a), self.b)

    @unittest.SkipTest
    def testando_merge(self):
        self.assertListEqual(merge_sort(self.a), self.b)

    def testando_heap(self):
        self.assertListEqual(heap_sort(self.a), self.b)

    @unittest.skip
    def testando_cocktail(self):
        self.assertListEqual(cocktail_sort(self.a), self.b)

    @unittest.skip
    def testando_quick(self):
        self.assertListEqual(quick_sort(self.a), self.b)

    @unittest.skip
    def testando_shell(self):
        self.assertListEqual(shell_sort(self.a), self.b)


if __name__ == "__main__":
    unittest.main()
