import time
import unittest
from random import randint

from micro_blockchain_demo import *


class BlockchainTestCase(unittest.TestCase):
    def setUp(self):
        self.blockchain = list()

    def test_untampered(self):
        populate_blockchain(self.blockchain, 10)
        blocks = [block for block in validate_blockchain(self.blockchain)]
        self.assertEqual(len(blocks), 0)

    def test_tamper(self):
        populate_blockchain(self.blockchain, 10)
        tamper_block = randint(3, 9)
        self.blockchain[tamper_block]['data'] = 'tamper, tamper!'
        blocks = [block for block in validate_blockchain(self.blockchain)]
        self.assertEqual(len(blocks), 10-(tamper_block+1))
