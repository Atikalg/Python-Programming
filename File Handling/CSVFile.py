import csv
'''
@Author: Atik Ahmed
@Date: 2022-06-19 10:10:10
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-19 10:10:10
@Title : CSV File Handling
'''
def create():
    with open("Details.csv", "w") as obj:
        file = csv.writer(obj)
        file.writerow(['Roll', 'Name', 'Marks'])
        while True:
            roll = int(input("Enter roll number"))
            name = input("Enter name")
            marks = int(input("Enter marks"))
            record = [roll, name, marks]
            file.writerow(record)
            check = int(input("1. Enter more\n2. Exit\nEter choice " ))
            if (check==2):
                break

def display():
    with open("Details.csv", "r") as obj:
        file = csv.reader(obj)
        for i in file:
            print(i)

if __name__ == "__main__":
    try:
        create()
        display()
    except Exception as e:
        print("Enter valid details", e)
