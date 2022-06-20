'''
@Author: Atik Ahmed
@Date: 2022-06-14 19:15:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 19:15:05
@Title : Prime Factorization
'''

def prime_factor(number):
    """
            :param count: User Name with 3 character
            :return: Print the String with User Name
            """
    j = 2
    for i in range(number // 2):
            while number % j == 0:
                print(j)
                number = int(number / j)
            j += 1

if __name__ == "__main__":
    number = int(input("Enter any number: "))
    prime_factor(number)