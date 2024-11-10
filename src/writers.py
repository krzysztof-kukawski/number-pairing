import os
from abc import abstractmethod, ABC


class FileWriter(ABC):

    @staticmethod
    @abstractmethod
    def write(output):
        pass


class TxtFileWriter(FileWriter):

    @staticmethod
    def write(output: list):
        output_path = os.path.join("data", "output.txt")
        with open(output_path, "w") as text_file:
            print(output, file=text_file)
