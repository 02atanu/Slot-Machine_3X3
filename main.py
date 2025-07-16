
import random
#Variables 
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":5,
    "D":6,
}

symbol_value = {
    "A":5,
    "B":3,
    "C":2,
    "D":1,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnig_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnig_lines.append(line + 1)
    return winnings, winnig_lines

def get_slot_machine_spin(rows, cols, symbols) :
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns= []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= "/")
            else:
                print(column[row], end= "")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? Rs. ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greeater that 0")
        else:
            print("Please enter a number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number!")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? Rs.")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}.")
        else:
            print("Please enter a number!")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do do not have enough, Your current balance is: Rs. {balance}")
        else:
            break    
    print(
        f"You are betting Rs. {bet} on {lines} lines. Total bet is Rs. {total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs. {winnings}")
    print(f"You won on", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is Rs. {balance}")
        answer = input("Press enter to play (Q to quit).")
        if answer == "Q":
            break
        balance += spin(balance)
    print(f"You left with Rs. {balance}")

    
main()