from abc import ABC, abstractmethod


#Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, level=0):
        pass

    @abstractmethod
    def display_ls(self):
        pass
