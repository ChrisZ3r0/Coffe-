# importing the module
import csv

user = []
balance = []
cardid = []

kave = []
buyable = []
price = []

def load_user_data():

# open the file in read mode
    filename = open('../data/payed.csv', 'r')

# creating dictreader object
    file = csv.DictReader(filename)

# creating empty lists

# iterating over each row and append
# values to empty list
    for col in file:
        user.append(col['user_name'])
        balance.append(col['balance'])
        cardid.append(col['card_id'])

# printing lists
    # print('User:', user)
    # print('Balance:', balance)
    # print('Cardid:', cardid)

def load_coffe():
    filename = open('../../data/kavek.csv', 'r')
    file = csv.DictReader(filename)
    for col in file:
        kave.append(col['coffe'])
        buyable.append(col['available'])
        price.append(col['price'])

    return kave,buyable,price

def checkdata(checking):
    load_user_data()
    if checking in cardid:
        print("True")
        return True
    else:
        print("false")
        return False