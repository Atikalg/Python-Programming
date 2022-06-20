'''
@Author: Atik Ahmed
@Date: 2022-06-18 11:10:10
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-18 11:10:10
@Title : Text File Handling
'''
def writeText():
    obj = open("abc.txt", "w")
    obj.write("Hello world")
    obj.close()

def appendWrite():
    obj = open("abc.txt", "a")
    obj.write(" welcome to python programming")
    obj.close()
def readText():
    obj = open("abc.txt", "r")
    print(obj.read())
    obj.close()

if __name__ == "__main__":
    writeText()
    appendWrite()
    readText()