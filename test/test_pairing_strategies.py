import unittest
from src.pairing_strategies import IterativePairing


class IterativePairingTest(unittest.TestCase):
    def test_create(self):

        good_numbers = [0, 12, 22, 11, 1, 8, 4]
        bad_numbers = [40, 10, 200, 1, 0, 0]

        good_pairs = IterativePairing.create(good_numbers, 12)
        bad_pairs = IterativePairing.create(bad_numbers, 12)

        assert len(good_pairs) == 3
        assert len(bad_pairs) == 0


if __name__ == "__main__":
    unittest.main()
