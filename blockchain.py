blockchain = [[1]]


def get_last_blockchain():
    return blockchain[-1]


def add_value(transaction_amount):
    blockchain.append([get_last_blockchain(), transaction_amount])


add_value(2)
add_value(3)
add_value(4)

print(blockchain)
