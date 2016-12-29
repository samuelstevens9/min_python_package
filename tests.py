import unittest,os

class TestSuite(unittest.TestCase):
    
    def test_simple(self):
        print "just a simple test"


if __name__ == "__main__":
    unittest.main()