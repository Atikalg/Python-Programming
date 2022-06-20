import time

'''
@Author: Atik Ahmed
@Date: 2022-06-18 18:10:10
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-18 18:10:10
@Title : Stopwatch program
'''
class Stopwatch:
    def watch(self):
        """
                Description:
                    This function calculate elapse time
                Parameter:
                    None
                Return:
                    Elapsed time
            """

        try:

            while True:
                start = int(input("Enter 1 to Start:"))

                startTime = time.time()

                stop = int(input("Enter 0 to Stop Time:"))

                endTime = time.time()

                timeElapsed = endTime - startTime

                print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")

                check= int(input("1. Continue\n2.stop"))
                if check == 2:
                    break



        except ValueError:

            print(" Invalid input ")


# Main method
if __name__ == '__main__':
    print("\nWelcome to Stopwatch")
    obj = Stopwatch()
    # calling Stopwatch function
    obj.watch()