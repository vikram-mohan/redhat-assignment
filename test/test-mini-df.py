import unittest
import os

class TestSum(unittest.TestCase):

    def test_mini_df(self):
        stream = os.popen('python3 ../mini-df.py')
        output = stream.read()

        #verify that the output is not empty
        self.assertTrue(output)

if __name__ == '__main__':
    unittest.main()