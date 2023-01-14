#Name : Malik Abdul Hadi
#Course : Compiler Construction
#Reg No: 200901053
#Section : B

import xml.etree.ElementTree as ET
import csv
class Parsing:
    def __init__(self):
        self.file = ET.parse("compiler.xml")
        self.root = self.file.getroot()
        self.Book = self.root.find("book")

    def Printing(self):
      with open("mycsv.csv" , "w",newline='') as file:
        readingcsv = csv.writer(file)
        readingcsv.writerow(["id","author","title","genre","price", "publish_date","description"])
        for child in self.file.getroot():
            print("ID OF THE BOOK :", child.attrib)
            print("AUTHOR OF THE BOOK :", child.find("author").text)
            print("TITLE OF THE BOOK :", child.find("title").text)
            print("DESCRIPTION OF THE BOOK: :", child.find("description").text)
            print("PRICE OF THE BOOK : ", child.find("price").text)
            print("GENRE OF THE BOOK :", child.find("genre").text)
            print("PUBLISHING DATE OF THE BOOK: ", child.find("publish_date").text)

            print()
            readingcsv.writerow([child.attrib['id'],
                                child.find("author").text,
                                child.find("title").text,
                               child.find("genre").text,child.find("price").text,
                               child.find("publish_date").text,
                               child.find("description").text]
                               )

    def writing(self):
        with open("parsed_data.txt", "w") as f:
            for child in self.file.getroot():
                print("ID OF THE BOOK: ", child.attrib)
                print("AUTHOR OF THE BOOK :", child.find("author").text)
                print("TITLE OF THE BOOK :", child.find("title").text)
                print("DESCRIPTION OF THE BOOK: :", child.find("description").text)
                print("PRICE OF THE BOOK :", child.find("price").text)
                print("GENRE OF THE BOOK :", child.find("genre").text)
                print("PUBLISHING DATE OF THE BOOK:", child.find("publish_date").text)

                print()

if __name__ == "__main__":
    parser = Parsing()
    parser.Printing()