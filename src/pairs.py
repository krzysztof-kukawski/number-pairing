from readers import FileReader
from pairing_strategies import PairingStrategy


class Pairs:

    def __init__(self, reader: FileReader, path: str) -> None:
        self.input_numbers = reader.read(path)

    def create(self, strategy: PairingStrategy, target) -> list[tuple]:
        return strategy.create(self.input_numbers, target)
