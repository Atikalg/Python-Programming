import math
'''
@Author: Atik Ahmed
@Date: 2022-06-15 19:15:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 19:15:05
@Title : Euclidean Distance between two points
'''

def calculate_distance(first_point, second_point):
    return math.sqrt(first_point * first_point + second_point * second_point)


if __name__ == "__main__":
    try:
        x = int(input("Enter the value of x coordinate: "))
        y = int(input("Enter the value of y coordinate: "))
        euclidean_distance = calculate_distance(x, y)
        print("Euclidean distance = ", euclidean_distance)
    except Exception as e:
        print("Enter valid input", e)