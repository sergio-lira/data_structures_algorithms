import hashlib
import datetime as date
        
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(str(self.timestamp).encode('utf-8') + 
                   str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()

    def __str__(self):
        return "Hash:{}\nDate:{}\nData:{}\n".format(
                self.hash,
                self.timestamp,
                self.hash)
    
class BlockChain:
        
    def __init__(self):
        self.chains = list()
        
    def initialize(self, index):
        self.chains.append([Block(date.datetime.now(), "Block 0", "0")])
        
    def add_block(self, index, data):
        new_date = date.datetime.now()
        previous_hash = self.chains[index][-1]
        new_block = Block(new_date, data, previous_hash)
        self.chains[index].append(new_block)
        
    def generate_n_blocks_at_index(self, index, n):
        for n in range(0, n):
            self.add_block(index, '#{}'.format(n))
        
    def interate_blockchain(self):
        for i, chain in enumerate(self.chains):
            print('--- Block Chain #{} ---'.format(i))
            for j, block in enumerate(chain):
                print('Block {}\n{}'.format(j, str(block)))
                           
print('<<< Test Case 1 >>>\n Adding 10 blocks at chain index 0\n')
my_block_chain = BlockChain()
my_block_chain.initialize(0)
my_block_chain.generate_n_blocks_at_index(0, 10)

print('<<< Test Case 2 >>>\n Testing a blockchain of a single block at index 1\n')
my_block_chain.initialize(1)
my_block_chain.generate_n_blocks_at_index(1, 0)
my_block_chain.interate_blockchain()

print('<<< Test Case 3 >>>\n Non intialized blockchian')
my_block_chain = BlockChain()
my_block_chain.interate_blockchain()