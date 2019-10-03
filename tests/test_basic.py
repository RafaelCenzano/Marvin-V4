from .context import marvin

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_core_func(self):
    	self.assertEqual(marvin.core.func(), "hello")


if __name__ == '__main__':
    unittest.main()