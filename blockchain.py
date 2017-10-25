import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # create genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # create a new block in the blockchain
        # @prop->proof
        # @prop->previous_hash
        # return new block

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': prevous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self):
        # create new transaction to go into a block
        # @prop->sender
        # @prop->recipient
        # @prop->amount
        # return index

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            })

        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        # create sha-256 of a block
        # @prop->block
        #return str(hashCode)

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        pass

    @property
    def last_block(self):
        # reaturn last block in a chain
        pass
