'''
@Author: Atik Ahmed
@Date: 2022-06-15 19:15:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 19:15:05
@Title : Print 2D Array
'''

def display_array(rows, columns):
    a = []

    for i in range(0, rows):
        b = []

        for j in range(0, columns):
            print("Enter the {} {} th element".format(i, j))
            c = int(input())
            b.append(c)
        a.append(b) #[[1,2],[3,4]]
    return a


if __name__ == "__main__":
    try:
        row = int(input("Enter no.of rows "))
        column = int(input("Enter no.of columns "))
        array_element = display_array(row, column)
        for i in range(len(array_element)):
            print(array_element[i])
        #print(array_element)
    except Exception as e:
        print("Enter correct input", e)
