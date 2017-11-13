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


if __name__ == '__main__':
    unittest.main()
