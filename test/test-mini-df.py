import unittest
import os, subprocess

class TestSum(unittest.TestCase):

    def test_mini_df(self):
        
        sp = subprocess.Popen(["python3",  "../mini-df.py", "./"], stdout=subprocess.PIPE)
        output, err = sp.communicate()

        print(output)
        #verify that the output is not empty
        self.assertTrue(str(output))
        self.assertFalse(err)
        sp.kill()
    
    def test_mini_df_prettyPrint(self):
        
        sp = subprocess.Popen(["python3",  "../mini-df.py", "-h", "./"], stdout=subprocess.PIPE)
        output, err = sp.communicate()

        print(output)
        
        #verify that the output is not empty
        self.assertTrue(str(output))
        self.assertFalse(err)
        sp.kill()

if __name__ == '__main__':
    unittest.main()