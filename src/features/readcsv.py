# importing the module
import csv

user = []
balance = []
cardid = []

def load_data():

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


def checkdata(checking):
    load_data()
    if checking in cardid:
        print("True")
        return True
    else:
        print("false")
        return False