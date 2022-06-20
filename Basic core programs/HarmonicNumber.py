'''
@Author: Atik Ahmed
@Date: 2022-06-14 18:45:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 18:45:05
@Title : Find nth harmonic number
'''

def harmonic(n):
    """
        :param count: Nth harmonic number
        :return: print the Nth harmonic value
        """
    number = 1.0
    total_value = 1

    for i in range(n-1):
        total_value = total_value + (1 / number + 1)
        number = number + 1
    return total_value


if __name__ == "__main__":
    n = int(input("Enter the value of n "))
    value = harmonic(n)
    print(value)