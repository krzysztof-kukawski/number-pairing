import os
from src.pairs import Pairs
from src.pairing_strategies import IterativePairing
from src.readers import TxtFileReader
from src.writers import TxtFileWriter

directory = os.path.dirname(__file__)
input_path = os.path.join(directory, "data" ,"input.txt")

pairs = Pairs(TxtFileReader, input_path)
found_pairs = pairs.create(IterativePairing, 12)

TxtFileWriter.write(found_pairs)
