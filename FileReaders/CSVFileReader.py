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
                if( len(row)<=0):
                    continue # for empty rows
                ls=ListingDetails(row[0],row[1],row[2],row[3],row[4],None)

                result.append(ls)
        return result

    def write(self, update_listings):
        with open(self.file_path, 'wb') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',', quotechar='|')
            file_writer.writerow(ListingDetails.header)

            for list in update_listings:
                file_writer.writerow([list.supplier, list.url, list.ebay_url, list.price, list.shipping])
                # row[3]= update_listings[index].price
                # row[4] = update_listings[index].shipping
                # row[5] = update_listings[index].is_in_stock
                # index=index+1
            #csvfile.close()



