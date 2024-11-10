import unittest
import os
from unittest.mock import mock_open, patch
from src.writers import TxtFileWriter


class TxtFileWriterTest(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_write(self, mock_open):
        test_input = [1, 2, 3]

        TxtFileWriter.write(test_input)
        output_path = os.path.join("data", "output.txt")
        mock_open.assert_called_once_with(output_path, "w")


if __name__ == "__main__":
    unittest.main()
