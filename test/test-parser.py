import unittest
from inputParser import parseInputs

class TestSum(unittest.TestCase):

    def test_parseInputs(self):
        arguments = ["-e", "//d", "DUMMYFILE"]
        args, optionsMap = parseInputs(arguments, "qe:")
        self.assertIsNotNone(args)
        self.assertIsNotNone(optionsMap)

    def test_parseInputs_options(self):
        arguments = ["-e", "//d", "DUMMYFILE"]
        _ , optionsMap = parseInputs(arguments, "qe:")
        self.assertIsNotNone(optionsMap)
        self.assertIsNotNone(optionsMap["-e"])

    def test_parseInputs_args(self):
        arguments = ["-e", "//d", "DUMMYFILE"]
        args , _ = parseInputs(arguments, "qe:")
        self.assertEqual(args[-1], "DUMMYFILE")

if __name__ == '__main__':
    unittest.main()