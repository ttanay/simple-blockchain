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

    def proof_of_work(self, last_proof):
        # hash of last_proof and proof shoul start with 4 '0's

        proof = 0
        while self.valid_proof(last_proof, prof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # checks if hash('{last_proof}{proof}') starts with '0000'

        guess = '{}{}'.format(last_proof, proof).encode()
        guess_hash = haslib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
