"""Program for creating CSV"""

# Import modules
import csv

def create_csv_file(filename:str(),rowlist):
    """To write csv file with the list provided"""
    # name should be filename.csv
    with open(filename, 'w', encoding="utf-8") as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|',
        quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # To calculate the coloums
        item_length = len(rowlist[0])
        for item in rowlist:
            # Write to row
            writer.writerow([item[count] for count in range(item_length)])

if __name__ == '__main__':
    print("This module executes as a standalone script")
    content= [('Anime', 'Main Character', 'Devil Fruit', 'Vice Captian')]
    CSVNAME = "luffy.csv"
    RESULT = create_csv_file(CSVNAME,content)
    print(RESULT)
else:
    pass
