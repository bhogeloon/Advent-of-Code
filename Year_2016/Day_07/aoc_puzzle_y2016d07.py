"""
Year 2016, Day 7

Problem description: See https://adventofcode.com/2016/day/7

The following classes are used:
- Sequence: Any sequence within the IPv7 address. This can be either normal
    or hypernet
- Ipv7Address: An IPv7 address, consisting of a list of normal Sequences and
    a list of hypernet Sequences
- Ipv7AddressList: List container class of Ipv7Adress objects.

Part 1: Split the input in normal and hypernet sequences. Then look for an
ABBA in the hypernet sequences. If so, no TLS support. If not, look for an 
ABBA in the normal sequences, If so, TLS is supported.

Part 2: Go through all normal sequences and collect all three letter 
combinations that adhere to aba. Then turn them inside out (bab) and go
through all hypernet sequences to see of such combination is part of the
sequence. If so: it supports SSL.
"""

# Imports
from __future__ import annotations
from pprint import pprint
import re


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Sequence:
    '''A number of characters forming a sequence'''

    def __init__(self, word: str) -> None:
        self.seq = word


    def is_abba(self) -> bool:
        '''Check if the sequence is an abba sequence'''
        for i in range(len(self.seq)-3):
            sub_seq = self.seq[i:i+4]

            if (
                sub_seq[0] == sub_seq[3] and
                sub_seq[1] == sub_seq[2] and
                sub_seq[0] != sub_seq[1]
            ):
                return True

        return False
    

    def get_aba(self) -> list:
        '''Return a list of three letter sequences which adhere to aba'''
        abas = []
        for i in range(len(self.seq)-2):
            sub_seq = self.seq[i:i+3]

            if (
                sub_seq[0] == sub_seq[2] and
                sub_seq[0] != sub_seq[1]
            ):
                abas.append(sub_seq)

        return abas
    

    def check_bab(self, aba: str) -> bool:
        '''Check if the word is part of the sequence'''
        # Reverse aba in bab
        bab = aba[1] + aba[0] + aba[1]
        return bab in self.seq


class Ipv7Address:
    '''Consists of a list of sequences and hypernet sequences'''

    def __init__(self, line:str) -> None:
        # 'Normal' sequences
        self.seqs = []
        # 'hypernet'sequences
        self.hyp_seqs = []
        # Split the line using the [ and ] characters
        seq_strs = re.split(r'[\[\]]', line)

        # The even numbers are now the normal ones
        for i in range(0,len(seq_strs), 2):
            self.seqs.append(Sequence(seq_strs[i]))

        # The uneven numbers are the hypernet ones
        for i in range(1,len(seq_strs), 2):
            self.hyp_seqs.append(Sequence(seq_strs[i]))


    def tls_support(self) -> bool:
        '''Check if the ip address supports TLS'''
        # If any hypernet sequence is abba, TLS is not supported
        for seq in self.hyp_seqs:
            if seq.is_abba():
                return False
            
        # Then check if there is an abba sequence in the normal ones
        for seq in self.seqs:
            if seq.is_abba():
                return True
            
        # If nothing found
        return False
    

    def ssl_support(self) -> bool:
        '''Check if the IP address supports SSL'''
        # This will contain the list of aba combinations
        abas = []
        for seq in self.seqs:
            abas.extend(seq.get_aba())

        # Check all combinations
        for aba in abas:
            for seq in self.hyp_seqs:
                if seq.check_bab(aba):
                    return True

        # If not found
        return False


class Ipv7AddressList(list[Ipv7Address]):
    '''A list container class of Ipv7Address objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Ipv7Address(line))


    def get_tls_ips(self) -> int:
        '''Return the amount of ips that support TLS'''
        nr = 0

        for ip in self:
            if ip.tls_support():
                nr += 1

        return nr
    

    def get_ssl_ips(self) -> int:
        '''Return the amount of ips that support SSL'''
        nr = 0

        for ip in self:
            if ip.ssl_support():
                nr += 1

        return nr


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    ips = Ipv7AddressList(lines)

    return ips.get_tls_ips()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    ips = Ipv7AddressList(lines)

    return ips.get_ssl_ips()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
