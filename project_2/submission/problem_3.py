from collections import Counter
import heapq
import sys

class Node():

    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key} {self.frequency}"

    def __lt__(self, other):
        return self.frequency < other.frequency

class HuffmanTree():

    def __init__(self, string):
        self.string = string
        self.frequency_table = self.get_char_frequency(string)
        self.heap = []
        self.encoder = {}
        self.decoder = {}
        self.root = None

    def map_codes(self, node, code):
        if node == None:
            return

        #Handling of special case where the tree is made of a single node
        if node.key and code=="":
            code = "0"

        if node.key:
            self.encoder[node.key] = code
            self.decoder[code] = node.key
            return

        self.map_codes(node.left, code + "0")
        self.map_codes(node.right, code + "1")

    def build_tree(self):
        if len(self.frequency_table) == 0:
            return

        for key, frequency in self.frequency_table:
            node = Node(key, frequency)
            heapq.heappush(self.heap, node)

        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)

            _new = Node(None, left.frequency + right.frequency)
            _new.left = left
            _new.right = right

            #print("left: {} \nright:{} \nnew:{}\n".format(left, right, _new))

            heapq.heappush(self.heap, _new)

        #Root will be the node left in the priority queue
        self.root = heapq.heappop(self.heap)
        self.map_codes(self.root, "")

    def encode_text(self):
        if self.root == None:
            return "", None

        return ''.join([self.encoder[char] for char in self.string]), self.root

    def decode_text(self, text):
        if self.root == None:
            return "", None

        running_code = ""
        decoded_text = ""
        for bit in text:
            running_code += bit
            if running_code in self.decoder:
                decoded_char = self.decoder[running_code]
                decoded_text += decoded_char
                running_code = ""

        return decoded_text

    def get_char_frequency(self, string):
       return sorted(Counter(string).items(), key=lambda _tuple: _tuple[1])

    def print_mapping(self):
        print("Encoding:")
        for key, value in self.encoder.items():
            print('key: {} value:{}'.format(key, value))

print("<<< Test Case 1 >>> ")
a_great_sentence = "The bird is the word"
test = HuffmanTree(a_great_sentence)
test.build_tree()
test.print_mapping()
print(f'\nInput: {test.string}\nCompressed text: {test.encode_text()}\n')
print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = test.encode_text()
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = test.decode_text(encoded_data)
print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("<<< Test Case 2 >>> ")
a_great_sentence = "010001001010010011101011101110"
test = HuffmanTree(a_great_sentence)
test.build_tree()
test.print_mapping()
print(f'\nInput: {test.string}\nCompressed text: {test.encode_text()}\n')
print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = test.encode_text()
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = test.decode_text(encoded_data)
print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("<<< Test Case 3 >>>")
a_great_sentence = ""
test = HuffmanTree(a_great_sentence)
test.build_tree()
test.print_mapping()
print(f'\nInput: {test.string}\nCompressed text: {test.encode_text()}\n')
print ("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = test.encode_text()
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = test.decode_text(encoded_data)
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("<<< Test Case 4 >>>")
a_great_sentence = "AAAAAAAAAAAAA"
test = HuffmanTree(a_great_sentence)
test.build_tree()
test.print_mapping()
print(f'\nInput: {test.string}\nCompressed text: {test.encode_text()}\n')
print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = test.encode_text()
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = test.decode_text(encoded_data)
print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
