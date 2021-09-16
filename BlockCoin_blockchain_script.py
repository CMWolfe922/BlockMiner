
def hash_function(s):
    b = s.encode()
    return hashlib.sha1(b).hexdigest()

hash_function('hello world')

def print_blockchain(blockchain):
    for i in range(len(blockchain)):
        print('Block %d: %s' % (i, blockchain[i].compute_hash()))

# CREATES SECURITY AND DATA INTEGRITY
def check_integrity():

    for i in range(1,len(blockchain)):
        h1 = blockchain[i-1].compute_hash()
        h2 = blockchain[i].previous_hash
        print('Block %d: %s => %s' % (i-1, h1, 'VALID' if (h1==h2) else 'WRONG'))

# CREATE MERKLE HASH TREE FOR ACCEPTING AS MANY TRANSACTIONS AS WE NEED:
def hash_tree(trx):
    """Transactions need to be defined/created before this is implemented"""
    if len(trx) == 1:
        return hash_function(trx[0])
    elif len(trx) == 2:
        return hash_function(trx[0] + trx[1])
    else:
        return hash_function(hash_tree(trx[:2]) + hash_tree(trx[2:len(trx)]))
# root_hash = hash_tree(transactions)
# root_hash


# NOW I WILL CREATE A FUNCTION FOR THE PRROF OF WORK ALGO
def PoW():
    # PROOF OF WORK
    base_string = 'Hello, World!' # What the PoW algo will work on solving
    nonce = -1
    h = ''

    while h[:3] != '000':
        nonce = nonce + 1
        s = base_string + str(nonce)
        h = hash_function(s)

    print('%s => %s' % (s, h))

#=================================================================#
# Create a function that creates the challenge and work
# for mining. Work should slowly increase.

def challenge():
    pass

def work():
    pass
#=================================================================#

# MINTING COINS --> works just like the PoW func
def mint(challenge, work):
    nonce = -1
    h = ''

    while h[:work] != '0'*work:
        nonce = nonce + 1
        h = hash_function(challenge + str(nonce))

    return nonce

# nonce = mint(challeng(), work())

# FUNCTION TO EVALUATE NEWLY MINTED BLOCKS
def evaluate(challenge, work, nonce):
    h = hash_function(challenge + str(nonce))
    return (h[:work] == '0'*work)

# evaluate('Hello, World!', 3, 898)
#====================================================================#

# CREATE THE BLOCK CLASS
class Block():

    def __init__(self, previous_hash, transactions, nonce):
        self.previous_hash = previous_hash
        self.root_hash = hash_tree(transactions)
        self.nonce = nonce
        self.transactions = transactions

    def __repr__(self):
        return self.__dict__.__repr__()

    def compute_hash(self):
        return hash_function(self.previous_hash + self.root_hash + str(self.nonce))
