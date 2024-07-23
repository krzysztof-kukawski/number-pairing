from abc import abstractmethod, ABC


class PairingStrategy(ABC):

    @staticmethod
    @abstractmethod
    def create(left: list, target: int):
        pass


class IterativePairing(PairingStrategy):

    @staticmethod
    def create(left: list, target: int) -> list[tuple]:
        pairs = []
        numbers_seen = set()

        for number in left:
            complement = target - number

            if complement in numbers_seen:
                pair = tuple(pair)
                pairs.append(pair)

            numbers_seen.add(number)

        return pairs
