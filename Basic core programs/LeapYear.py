'''
@Author: Atik Ahmed
@Date: 2022-06-14 18:20:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 18:20:05
@Title : Leap year program
'''

def leap_year(year):
    """
        :param count: Take the year as input
        :return: print the year is leap or not
        """
    if len(year)==4:
        if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0:
            print("This is leap year")
        else :
            print("This is not leap year")
    else :
        print("Invalid input,please enter a four digit number")


if __name__ == "__main__":
    year = input("Enter a year ")
    result = leap_year(year)
