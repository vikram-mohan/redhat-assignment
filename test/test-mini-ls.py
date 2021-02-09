import unittest
import os, subprocess

class TestSum(unittest.TestCase):

    def test_mini_ls(self):
        sp = subprocess.Popen(["python3",  "../mini-ls.py", "../"], stdout=subprocess.PIPE)
        output, err = sp.communicate()

        #verify that the output is not empty
        self.assertTrue(output)
        self.assertFalse(err)

        sp.kill()

    def test_mini_recursive(self):
        sp = subprocess.Popen(["python3",  "../mini-ls.py", "-r", "./"], stdout=subprocess.PIPE)
        output, err = sp.communicate()
        
        #verify that the output is not empty
        self.assertIsNotNone(output)
        self.assertFalse(err)

        sp.kill()

if __name__ == '__main__':
    unittest.main()