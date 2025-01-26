from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
        # print("This abstract start ....")


com1 = Computer()
com1 .process()