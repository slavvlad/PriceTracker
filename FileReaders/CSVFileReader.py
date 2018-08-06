import FileReaders.SourceFileReader
import csv
from ListingDetails import ListingDetails
from Singleton import Singleton

@Singleton
class CSVFileReader(FileReaders.SourceFileReader.FileReader):

    # def __init__(self,path):
    #     super(CSVFileReader, self).__init__(path)
    def read(self):
        result=[]
        with open(self.file_path, 'rb') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(file_reader)#skip the headers
            for row in file_reader:
                ls=ListingDetails(row[0],row[1],row[2],row[3],None)

                result.append(ls)
        return result




