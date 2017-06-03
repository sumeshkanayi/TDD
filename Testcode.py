from code import *  # import everything from your module
import unittest  # This loads the testing methods and a main program


class TestMultiplier(unittest.TestCase):  # use any meaningful name

 def testmultiplier(self):
        self.assertEqual(4, multiplier(2, 2))

 def testmultiply_two_negative_numbers(self):
     self.assertEqual(25, multiplier(-5, -5))

 def testmultiply_positive_and_negative_numbers(self):
     self.assertEqual(-50, multiplier(-5, 10))


if __name__ == '__main__':
    unittest.main()

