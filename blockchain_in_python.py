import hashlib
import random
from time import time
from Crypto.Signature import PKCS1_v1_5

class Block:
    def __init__(self,prev_hash,transactions):
        self.transactions=transactions
        self.prev_hash=prev_hash
        self.data=",".join(transactions)+","+prev_hash
        self.hash=hashlib.sha256(self.data.encode()).hexdigest()

private_keys = {
    "Alice": 110011011101,
    "Benjamin": 001010100111,
    "Charlotte": 010011010100,
    "Daniel": 111000110101,
    "Emily": 000111001010,
    "Felix": 101010010110,
    "Grace": 111100110001,
    "Henry": 000011011010,
    "Isabella": 011101011100,
    "James": 010110101001,
    "Katherine": 111111000101,
    "Liam": 001101011111,
    "Mia": 101000111000,
    "Noah": 010101100011,
    "Olivia": 111101011010,
    "Peter": 000010110001,
    "Quinn": 110111100100,
    "Sophia": 101010100011,
    "Thomas": 011010111000,
    "Victoria": 100100111111
}
public_keys = {
    "Alice": 101110010110,
    "Benjamin": 011001010011,
    "Charlotte": 100101001001,
    "Daniel": 111110001011,
    "Emily": 001010100101,
    "Felix": 110101000111,
    "Grace": 000111110100,
    "Henry": 011001100111,
    "Isabella": 101011010101,
    "James": 111010011000,
    "Katherine": 010100011010,
    "Liam": 001011100110,
    "Mia": 111000101011,
    "Noah": 010010110010,
    "Olivia": 100111101010,
    "Peter": 111000100001,
    "Quinn": 000101011100,
    "Sophia": 011010001110,
    "Thomas": 100110011000,
    "Victoria": 010011001111
}
transactions=[]
users=["Alice","Benjamin","Charlotte","Daniel","Emily","Felix","Grace","Henry","Isabella","James","Katherine","Liam","Mia","Noah","Olivia","Peter","Quinn","Sophia","Thomas","Victoria"]
numbers = [random.randint(1, 100) for i in range(20)]
x=input("how many transactions per block?: ")
transaction=""
user1=""
number=""
for i in x:
    number=random.choice(numbers)
    user1=random.choice(users)
    transaction=f"{user1} pays {number} GHOUL to {random.choice(users)}"
    transactions.append()
block1=Block("",transactions)
print(block1.hash)
