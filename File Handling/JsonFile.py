import json
'''
@Author: Atik Ahmed
@Date: 2022-06-19 10:30:00
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-19 10:30:00
@Title : JSON File Handling
'''
def create():
    details = {
        "name" : "Atik",
        "roll_number" : 101,
        "marks" : 100
    }
    file = json.dumps(details, indent=3)
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(file)

def display():
    with open("sample.json", "r") as fileread:
        print(fileread.read())

if __name__ == "__main__":
    create()
    display()


