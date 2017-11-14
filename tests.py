import unittest


class TestStrMethods(unittest.TestCase):
    def test_split(self):
        s = 'IO-42 IKS Lab3'
        self.assertEqual(s.split(), ['IO-42', 'IKS', 'Lab3'])

    def test_join(self):
        values = ['IO-42', 'IKS', 'Lab3']
        self.assertEqual(' '.join(values), 'IO-42 IKS Lab3')


class TestMathMethods(unittest.TestCase):
    def test_max(self):
        l = [1, 4, 5, 2, 6, 3, 0]
        value_max = max(l)
        self.assertEqual(value_max, 6)


class TestListComprehentions(unittest.TestCase):
    def test_range(self):
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(test_list, list(range(10)))

    def test_example_comprehentions(self):
        test_list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        test_list2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
        test_list3 = [0, 4, 16, 36, 64]
        self.assertEqual(test_list1, [x**2 for x in range(10)])
        self.assertEqual(test_list2, [2**i for i in range(13)])
        self.assertEqual(test_list3, [x for x in test_list1 if x % 2 == 0])


class TestSlices(unittest.TestCase):
    def test_slices1(self):
        test_list = range(10)
        self.assertEqual(list(test_list[::2]), [0, 2, 4, 6, 8])

    def test_slices2(self): 
        test_list = range(10)
        self.assertEqual(list(test_list[::-1]), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
