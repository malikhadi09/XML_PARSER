# XML_PARSER

# EXPLANATION OF THE CODE:

This code is a script that parses an XML file named "compiler.xml" that is given in the assignment , and in this code it writes the data from the XML file to both a CSV file named "mycsv.csv" and a text file named "parsed_data.txt". It uses the xml.etree.ElementTree library to parse the XML file, and we have defined a class called Parsing which has an init method that initializes the class by parsing the XML file and getting its root element. It also has two methods mentioned below,
First method is Printing method.
And the Second method is Writing method.
Let’s talk about The Printing method first, in printing method class what we do is opens a CSV file and writes the headers for the columns. It then loops through each child element of the root element, extracting the data from each element, printing it to the console and writing it to the CSV file.
And next, the writing method does the same thing but writes the data to a text file. 
In the last if block, an instance of the Parsing class is created, and the Printing method is called on it.

# OUTPUT OF THE CODE:

![image](https://user-images.githubusercontent.com/92660593/212483158-a0907f9e-b686-4c2d-8b70-c258de862f46.png)
![image](https://user-images.githubusercontent.com/92660593/212483172-cfdd8e75-2539-459d-aefb-cf375c6feb78.png)
![image](https://user-images.githubusercontent.com/92660593/212483173-fe131d85-5e10-4c8c-a330-23da630d6629.png)
![image](https://user-images.githubusercontent.com/92660593/212483180-425ae62e-75ab-43a9-a7ef-d8c7aa6e2715.png)
![image](https://user-images.githubusercontent.com/92660593/212483185-4aaf9e10-8634-4113-9918-e063ac4a3d50.png)
![image](https://user-images.githubusercontent.com/92660593/212483190-d1e2726f-d521-4a47-bc57-1a62e02f6bcb.png)

# OUTPUT OF MYCSV.EXCEL FILE : 

![image](https://user-images.githubusercontent.com/92660593/212483208-b7ecae46-4f5a-4a20-9512-35648b926fb6.png)
