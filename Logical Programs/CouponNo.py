import random
'''
@Author: Atik Ahmed
@Date: 2022-06-17 18:10:10
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-17 18:10:10
@Title : Random coupon number generated
'''
class Coupon:
    def generate_coupon(self,lower, upper, number):
        coupon_numbers = set([])
        for i in range(number):
            coupon = random.randint(lower, upper)
            coupon_numbers.add(coupon)

        return coupon_numbers


if __name__ == "__main__":
    coupon = Coupon()
    lower_range = int(input("Enter the lower range: "))
    upper_range = int(input("Enter the upper range: "))
    number = int(input("Enter number of unique coupon numbers to generate: "))
    list = coupon.generate_coupon(lower_range, upper_range, number)
    print(list)