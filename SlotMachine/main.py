import random


MAX_LINES = 3 #constant value
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

#dict
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): 
        # dot items gives you key and value associted with it
        for _ in range(symbol_count): 
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #to copy a list, we use this operators using slice. 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #enumerate gives u index accordingly.
            if i != len(columns)  - 1:
               print(column[row], end=" | ")
            else: 
                print(column[row], end="")   

        print()    

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

def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines to bet on ( 1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
     return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}- ${MAX_BET}.")
        else:
            print("Please enter a Bet amount: ")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough balance. Current balance is: ${balance}")
        else:
            break    
            
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
