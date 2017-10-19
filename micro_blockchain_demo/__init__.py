import hashlib
import json
import time

def block_hash(block):
    """Calculate the SHA256 hash for a given block.

    Arguments:
        block -- dict representing the block

    Returns:
        hexadecimal representation of the hash (string)
    """
    m = hashlib.md5()
    m.update(block['previous_block_hash'])
    m.update(block['data'])
    m.update(json.dumps(block['metadata'], sort_keys=True))
    return m.hexdigest()


def validate_blockchain(blockchain):
    """Validate blockchain integrity. This is a generator that yields
    blocks that fail the integrity check.

    Arguments:
        blockchain -- the list of ordered blocks
    """
    result = {'failed_blocks': []}
    failed = False
    for i, block in enumerate(blockchain):
        if i == 0:
            continue

        if failed:
            yield blockchain[i-1]
        elif block['previous_block_hash'] != block_hash(blockchain[i-1]):
            yield blockchain[i-1]
            failed = True


def populate_blockchain(blockchain, block_count):
    """Append demo blocks to the blockchain.

    Arguments:
        blockchain -- the list where to append blocks to
        block_count -- number of blocks to generate
    """
    for i in range(len(blockchain), len(blockchain) + block_count):
        # genesis block
        previous_block_hash = '0'*32

        if i > 0:
            previous_block_hash = block_hash(blockchain[i-1])

        new_block = {
            'metadata': {
                'block_number': i,
                'create_date': time.time()
            },
            'data': 'random data for block %d' % (i,),
            'previous_block_hash': previous_block_hash
        }
        blockchain.append(new_block)
