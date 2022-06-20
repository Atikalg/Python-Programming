import random

'''
@Author: Atik Ahmed
@Date: 2022-06-14 18:10:10
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 18:10:10
@Title : Flip coin percentage
'''


def flip_coin(count):
    """
    :param count: number of times to flip the coin
    :return: head percentage
    """
    head = 0
    tail = 0
    for i in range(count):
        random_num = random.randint(0,1)

        if random_num == 1:
            head += 1
        tail += 1
    head_percentage = head / count * 100
    return head_percentage


if __name__ == "__main__":
    count = int(input("Enter number of times to flip the coin "))
    head_percentage = flip_coin(count)
    print("Tail percentage is = {}% ".format(100-head_percentage))
    print("Head percentage is = {}% ".format(head_percentage))

