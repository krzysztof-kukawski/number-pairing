import unittest
import os
from readers import TxtFileReader


class TxtFileReaderTest(unittest.TestCase):
    def test_read(self):
        directory = os.path.dirname(__file__)
        test_input_path = os.path.join(directory, "data", "test_input.txt")

        expected = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
        actual = TxtFileReader.read(test_input_path)

        assert actual == expected


if __name__ == "__main__":
    unittest.main()
