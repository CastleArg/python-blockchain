blockchain = []


def get_transaction_amount():
    return float(input('enter amount:'))


def get_user_choice():
    return input('your choice:')


def get_last_blockchain_value():
    """ does some stuff"""
    if len(blockchain) < 1:
        return None
    return 0 if len(blockchain) == 0 else blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction is None:
        return [1]
    blockchain.append([last_transaction, transaction_amount])


def print_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)


# def verify_chain():
#     block_index = 0
#     for block in blockchain:
#         print('Outputting block')
#         print(block)



tx_amount = get_transaction_amount()
add_transaction(tx_amount)

while True:
    print('Please choose')
    print('1: add a transaction')
    print('2: output blockchain')
    print('h: hack a past transaction')
    print('q: quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_amount()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('invalid')
print('done!')
