
def deposit():
    while True:
        amount = input("What will you like to deposit? $") #always gets text/string as an input. ex 45 is "45"
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero")
        else:
            print("Please enter a number.")
    return amount 
 
#The .isdigit() method is a handy tool used to check if a string consists entirely of numerical digits ($0-9$).Since input() always returns a string, .isdigit() is the most common way to "sanatize" user data before you try to convert it to an integer.How it WorksIt returns a Boolean (True or False). 

def main():
    balance = deposit()

main()

