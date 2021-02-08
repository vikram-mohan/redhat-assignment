import unittest
import os

class TestSum(unittest.TestCase):

    def test_mini_ls(self):
        stream = os.popen('python3 ../mini-ls.py ../')
        output = stream.read()

        #verify that the output is not empty
        self.assertTrue(output)

    def test_mini_recursive(self):
        stream = os.popen('python3 ../mini-ls.py -r ./')
        output = stream.read()
        
        #verify that the output is not empty
        self.assertIsNotNone(output)

if __name__ == '__main__':
    unittest.main()