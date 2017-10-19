import random
import cmd

import colors as color

from micro_blockchain_demo import *


class InteractiveBlockchain(cmd.Cmd, object):
    """This class represents the interactive app
    """
    def __init__(self):
        """Constructor
        """
        super(InteractiveBlockchain, self).__init__()
        self.blockchain = list()
        self.do_populate('')

    def do_clear(self, line):
        """Clear the blockchain
        """
        self.blockchain = list()
        print color.green('Cleared')

    def do_print(self, line):
        """Print the blockchain: print [<block number>]
        If block number is not specified, print all blocks.
        """
        if len(self.blockchain) > 0:
            if line:
                try:
                    index = int(line)
                    if index < 1 or index > len(self.blockchain)-1:
                        raise ValueError()
                except ValueError:
                    print color.red('Invalid block number')
                    return False
                else:
                    print '%s: %s' % (
                        color.yellow(block_hash(self.blockchain[index])),
                        color.cyan(self.blockchain[index]),)
            else:
                for block in self.blockchain:
                    print '%s: %s' % (
                        color.yellow(block_hash(block)),
                        color.cyan(block),)
        else:
            print color.green('Empty blockchain')

    def do_populate(self, line):
        """Populate the blockchain: populate [<block count>]
        If block count is not specified, a random amount of blocks
        will be created.
        """
        try:
            count = int(line)
        except ValueError:
            count = random.randint(3, 100)
        print color.green('Appending %d random blocks' % (count,))
        populate_blockchain(self.blockchain, count)

    def do_tamper(self, line):
        """Tamper block: tamper [<block number>]
        If block number is not specified, a random block will be tampered.
        """
        try:
            index = int(line)
        except ValueError:
            if len(self.blockchain) < 3:
                print color.red('Blockchain size is too small')
                return False
            index = random.randint(1, len(self.blockchain)-1)

        print color.red('Tampering a block %d!' % (index,))
        print color.magenta('Before:')
        print '%s: %s' % (
            color.yellow(block_hash(self.blockchain[index])),
            color.cyan(self.blockchain[index]),)
        self.blockchain[index]['data'] = 'tamper, tamper!'
        print color.magenta('After:')
        print '%s: %s' % (
            color.yellow(block_hash(self.blockchain[index])),
            color.cyan(self.blockchain[index]),)

    def do_check(self, line):
        """Run integrity on blockchain and print bad blocks.
        """
        counter = 0
        for block in validate_blockchain(self.blockchain):
            print '%s: %s' % (
                color.red(block_hash(block)),
                color.cyan(block),)
            counter += 1
        if counter > 0:
            print color.red('(total bad blocks: %d)' % (counter,))
        else:
            print color.green('Blockchain integrity check passed')

    def do_quit(self, line):
        """Exit the app
        """
        return True

    def do_q(self, line):
        """Exit the app
        """
        return self.do_quit(line)


def main():
    InteractiveBlockchain().cmdloop()


if __name__ == '__main__':
    main()
