import re
from abc import abstractmethod, ABC


class FileReader(ABC):

    @staticmethod
    @abstractmethod
    def read(path: str):
        pass


class TxtFileReader(FileReader):

    @staticmethod
    def read(path: str) -> list[int]:
        with open(path) as file:
            text = file.read()

            numbers = re.findall(r'\d+', text)
            numbers = [int(i) for i in numbers]

            return numbers
