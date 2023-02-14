#! /usr/bin/env python

from .solidity_types import address as HexAddress
from typing import Dict, List, Optional, Sequence, Tuple, Union

class Credentials:
    def __init__(self, address:HexAddress, private_key:str ='', nickname=''):
        self.address = address
        self.private_key = private_key
        self.nickname = nickname

    def short_address(self):
        return f'{self.address[0:6]}…{self.address[-4:]}'

    def __repr__(self):
        return f'{self.nickname:<10}:  {self.address}'

    @staticmethod
    def cred_for_nickname(creds:Sequence['Credentials'], nickname:str) -> Optional['Credentials']:
        result = None
        for cred in creds:
            if cred.nickname == nickname:
                result = cred
                break
        return result

    @staticmethod
    def cred_for_address(creds:Sequence['Credentials'], address:HexAddress) -> Optional['Credentials']:
        result = None
        for cred in creds:
            if cred.address == address:
                result = cred
                break
        return result        
