import math
'''
@Author: Atik Ahmed
@Date: 2022-06-15 19:15:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-15 19:15:05
@Title : Quadratic equation calculation
'''

def calculate_root(a, b, c):
    delta = b * b - 4 * a * c
    first_root = (-b + math.sqrt(delta)) / 2 * a
    second_root = (-b - math.sqrt(delta)) / 2 * a

    return first_root, second_root


if __name__ == "__main__":
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        first_root, second_root = calculate_root(a, b, c)
        print(first_root, second_root)
    except Exception as e:
       print("Enter valid input", e)