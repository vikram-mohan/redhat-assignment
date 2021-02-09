import unittest
import os, subprocess

class TestSum(unittest.TestCase):

    def test_mini_grep(self):
        sp = subprocess.Popen(["python3",  "../mini-grep.py", "-e", "[0-9]",  "./data.txt"], stdout=subprocess.PIPE)
        output, err = sp.communicate()

        #verify that the output is not empty
        self.assertTrue(str(output))
        self.assertFalse(err)

        sp.kill()
    
    def test_mini_grep_withLineNo(self):
        sp = subprocess.Popen(["python3",  "../mini-grep.py", "-q", "-e", "[0-9]",  "./data.txt"], stdout=subprocess.PIPE)
        output, err = sp.communicate()

        #verify that the output is not empty
        self.assertIn("line no", str(output))
        self.assertFalse(err)

        sp.kill()

    def test_mini_grep_withInvalidFile(self):
        sp = subprocess.Popen(["python3",  "../mini-grep.py", "-q", "-e", "[0-9]",  "./INVALID.txt"], stdout=subprocess.PIPE)
        output, _ = sp.communicate()

        #verify that the output is not empty
        self.assertIn("Unexpected inputs: Invalid Path", str(output))

        sp.kill()

    def test_mini_grep_withInvalidOption(self):
        sp = subprocess.Popen(["python3",  "../mini-grep.py", "-r", "-q", "-e", "[0-9]",  "./INVALID.txt"], stdout=subprocess.PIPE)
        output, _ = sp.communicate()

        #verify that the output is not empty
        self.assertIn("Unexpected inputs: The provided option is not supported", str(output))

        sp.kill() 

if __name__ == '__main__':
    unittest.main()