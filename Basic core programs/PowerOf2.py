'''
@Author: Atik Ahmed
@Date: 2022-06-14 18:45:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 18:45:05
@Title : Print the table power of 2
'''

def power_of_2(number,num):
    if (num<=31 & num>=0):
        for i in range(num-1):
            number = number * 2
        return number
    else :
        return "Enter value of N between 0 to 31"

if __name__ == "__main__":
    num = int(input("Enter the value of N "))
    total_value = power_of_2(2,num)
    print(total_value)