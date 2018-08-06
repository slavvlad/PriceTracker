import FileReaders.SourceFileReader
import csv
import ListingDetails

class CSVFileReader(FileReaders.SourceFileReader.FileReader):

    def __init__(self,path):
        super(CSVFileReader, self).__init__(path)
    def read(self):
        result=[]
        with open(self.file_path, 'rb') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in file_reader:
                ls=ListingDetails()
                ls.supplier = row["supplier"]
                ls.url = row["url"]
                ls.cost = row["price"]
                ls.shipping = row["shipping"]
                result.append(ls)





