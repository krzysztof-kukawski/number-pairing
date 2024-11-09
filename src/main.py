import os
from pairs import Pairs
from pairing_strategies import IterativePairing
from readers import TxtFileReader
from writers import TxtFileWriter

directory = os.path.dirname(__file__)
input_path = os.path.join(directory, "input.txt")

pairs = Pairs(TxtFileReader, input_path)
found_pairs = pairs.create(IterativePairing, 12)

TxtFileWriter.write(found_pairs)
