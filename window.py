from abc import ABC, abstractmethod, abstractproperty
import displayio as dio

class Window(ABC):

    @abstractproperty
    def group(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    @abstractmethod
    def deinit(self):
        pass