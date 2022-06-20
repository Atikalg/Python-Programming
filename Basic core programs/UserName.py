'''
@Author: Atik Ahmed
@Date: 2022-06-14 20:00:05
@Last Modified by: Atik Ahmed
@Last Modified time: 2022-06-14 20:00:05
@Title : Replace username with string
'''

def replace(username):
    """
        :param count: User Name with 3 character
        :return: Print the String with User Name
        """
    if(len(username) < 3):
        return "username is not less then 3 char"
    else:
        return "Hello " +username+ " How are you?"

if __name__ == "__main__":
    username = input("enter the name: ")
    message = replace(username)
    print(message)