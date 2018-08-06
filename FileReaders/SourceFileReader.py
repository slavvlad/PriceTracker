from abc import ABCMeta, abstractmethod

class FileReader():
     __metaclass__ = ABCMeta
     def __init__(self,file_path):
         self.file_path = file_path
     @abstractmethod
     def read(self):
       pass