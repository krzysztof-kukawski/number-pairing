from abc import abstractmethod, ABC


class FileWriter(ABC):

    @staticmethod
    @abstractmethod
    def write(output):
        pass


class TxtFileWriter(FileWriter):

    @staticmethod
    def write(output: list):
        with open("Output.txt", "w") as text_file:
            print(output, file=text_file)
