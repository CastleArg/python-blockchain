from webbrowser import get


blockchain = []


def get_last_blockchain_value():
    return 0 if len(blockchain) == 0 else blockchain[-1] 


def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])

tx_amount = input('enter amount:');
add_value(float(tx_amount))

print(blockchain)