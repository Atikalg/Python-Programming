import random
"""
    @Author: Atik Ahmed
    @Date: 2022-06-17 21:55:00
    @Last Modified by: Atik Ahmed
    @Last Modified time: 2022-06-17 21:56:00
    @Title : Gambler
"""
class Gamble:

    def gambling(self,stake, goal):
        """
               Simulates a gambler who start with $stake and place fair $1 bets until
                    he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
                    times he/she wins and the number of bets he/she makes.
           :param stake: Take input as player stack
           :param goal: winning goal
           :return: none
           """
        win_count = loss_count = game_count = 0
        while stake != 0 and stake != goal:
            game_result = random.random()
            if game_result <= 0.5:
                stake += 1
                win_count += 1
                game_count += 1
            else:
                stake -= 1
                loss_count += 1
                game_count += 1
        win_percentage = win_count/game_count*100
        loss_percentage = loss_count/game_count*100
        print("Win percentage is ", win_percentage)
        print("Loss percentage is ", loss_percentage)
        print("Win count is ", win_count)



if __name__ == "__main__":
    stake = float(input("Enter the stake you have: "))
    goal = float(input("Enter your goal amount: "))

    gamble = Gamble()
    gamble.gambling(stake, goal)
