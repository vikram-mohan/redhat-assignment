import unittest
import os

class TestSum(unittest.TestCase):

    def test_mini_grep(self):
        stream = os.popen('python3 ../mini-grep.py -e \\d ./data.txt')
        output = stream.read()

        #verify that the output is not empty
        print(output)
        self.assertTrue(output)
    
    def test_mini_grep_withLineNo(self):
        stream = os.popen('python ../mini-grep.py -q -e \\d ./data.txt')
        output = stream.read()

        #verify that the output is not empty
        print(output)
        self.assertIn("line no", output, "Line No information not found")

if __name__ == '__main__':
    unittest.main()