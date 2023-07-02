temp = []
bank = {}


def add_to_bank(name):
    bank[name] = 0


def deposit(name, sum):
    if name not in bank:
        add_to_bank(name)
    bank[name] += int(sum)


def withdraw(name, sum):
    if name not in bank:
        add_to_bank(name)
    bank[name] -= int(sum)


def transfer(name1, name2, sum):
    if name1 not in bank:
        add_to_bank(name1)
    if name2 not in bank:
        add_to_bank(name2)
    withdraw(name1, sum)
    deposit(name2, sum)


def balance(name):
    if name in bank:
        print(bank[name])
    else:
        print("ERROR")


def income(p):
    for name in bank:
        if bank[name] > 0:
            bank[name] = int(bank[name] * (1 + int(p)/100))


with open("input.txt", "r") as f:
    for line in f:
        temp = list(map(str, line.split()))
        if len(temp) != 0:
            if temp[0] == "DEPOSIT":
                deposit(temp[1], temp[2])
            elif temp[0] == "WITHDRAW":
                withdraw(temp[1], temp[2])
            elif temp[0] == "BALANCE":
                balance(temp[1])
            elif temp[0] == "TRANSFER":
                transfer(temp[1], temp[2], temp[3])
            elif temp[0] == "INCOME":
                income(temp[1])

