import os
from pairs import Pairs
from pairing_strategies import IterativePairing
from readers import TxtFileReader
from writers import TxtFileWriter

input_path = os.path.dirname(__file__) + r"\input.txt"
pairs = Pairs(TxtFileReader, input_path)
found_pairs = pairs.create(IterativePairing, 12)

TxtFileWriter.write(found_pairs)