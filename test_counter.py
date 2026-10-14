import unittest
from lab3_normal_num10_counter import Counter


class TestCounter(unittest.TestCase):
    def test_increase(self):
        counter = Counter()
        counter.increase()
        self.assertEqual(counter.value, 1)

    def test_decrease(self):
        counter = Counter()
        counter.decrease()
        self.assertEqual(counter.value, -1)


if __name__ == "__main__":
    unittest.main()