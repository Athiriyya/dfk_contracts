#! /usr/bin/env python

from .solidity_types import address as HexAddress
from typing import Dict, List, Optional, Sequence, Tuple, Union, cast

class Credentials:
    def __init__(self, address:HexAddress|str, private_key:str ='', nickname:str=''):
        self.address:HexAddress = cast(HexAddress, address)
        self.private_key = private_key
        self.nickname = nickname

    def short_address(self):
        return f'{self.address[0:6]}…{self.address[-4:]}'

    def __repr__(self):
        return f'{self.nickname:<10}:  {self.address}'

    def matches_abbreviation(self, query:str) -> bool:
        # An 'abbreviation' is a string that has the same beginning 
        # as self.nickname, case-insensitive, e.g. 'sli' for 'Slipfoot'
        return self.nickname.lower().startswith(query.lower())

    @staticmethod
    def cred_for_nickname(creds:Sequence['Credentials'], nickname:str, accept_abbreviation=True) -> 'Credentials':
        if accept_abbreviation:
            gen = (c for c in creds if c.matches_abbreviation(nickname))
        else:
            gen = (c for c in creds if c.nickname == nickname)
        try:
            return next(gen)
        except StopIteration:
            raise ValueError(f'Nickname {nickname} not found in {creds}')

    @staticmethod
    def cred_for_address(creds:Sequence['Credentials'], address:HexAddress) -> 'Credentials':
        gen = (c for c in creds if c.address == address)
        try:
            return next(gen)
        except StopIteration:
            raise ValueError(f'Address {address} not found in {creds}')   


    @staticmethod 
    def creds_for_nicknames(creds:Sequence['Credentials'], nicknames:Sequence[str], accept_abbreviation=True) -> List['Credentials']:
        creds_out = []
        for n in nicknames:
            try:
                c = Credentials.cred_for_nickname(creds, n, accept_abbreviation)
                creds_out.append(c)
            except ValueError:
                pass
        return creds_out
