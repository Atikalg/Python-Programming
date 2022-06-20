import math
'''
@Author: Atik Ahmed
@Date: 2022-06-15 19:15:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-15 19:15:05
@Title : Write a program wind_chill.py that takes two input from user as t
            and v and prints the wind chill
'''



def calculate_wind_chill(temp, vel):
    """
        :param speed: take input velocity from user
        :param temp: take input temperature from user
        :return: Chill wind (Temperature)
        """
    if 3 <= vel <= 120 and temp < 50:
        return 35.74 + (0.6215 * temp) + (0.4275 * temp - 35.75) * (math.pow(vel, 0.16))
    else:
        return "\nVelocity should be in range 3 - 120 mile/hr \nTemperature should be less than 50 F\n"


if __name__ == "__main__":
    try:
        temperature = float(input("Enter the value of temperature(in fahrenheit): "))
        velocity = float(input("Enter the value of velocity(in miles per hour): "))
        wind_chill = calculate_wind_chill(temperature, velocity)
        print("Effective temperature is: ", wind_chill)
    except Exception as e:
        print("Enter valid input", e)